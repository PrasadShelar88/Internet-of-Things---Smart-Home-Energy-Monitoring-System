import React, { useEffect, useMemo, useState } from 'react';
import { createRoot } from 'react-dom/client';
import { Activity, AlertTriangle, BatteryCharging, Database, Download, Gauge, IndianRupee, PlugZap, Power, RefreshCw, Trash2, Zap } from 'lucide-react';
import './styles.css';

const API_BASE = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000';

async function api(path, options = {}) {
  const res = await fetch(`${API_BASE}${path}`, {
    headers: { 'Content-Type': 'application/json', ...(options.headers || {}) },
    ...options,
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(text || `Request failed: ${res.status}`);
  }
  return res.json();
}

function fmt(value, digits = 2) {
  const n = Number(value || 0);
  return Number.isFinite(n) ? n.toFixed(digits) : '0.00';
}

function Card({ title, value, unit, icon: Icon, tone = '' }) {
  return (
    <div className={`card ${tone}`}>
      <div className="cardTop">
        <span>{title}</span>
        <Icon size={22} />
      </div>
      <div className="cardValue">{value}<small>{unit}</small></div>
    </div>
  );
}

function App() {
  const [latest, setLatest] = useState(null);
  const [summary, setSummary] = useState(null);
  const [readings, setReadings] = useState([]);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState('');
  const [manual, setManual] = useState({ appliance: 'Main Circuit', voltage: 230, current: 2.5, duration_minutes: 1 });
  const [thresholds, setThresholds] = useState({ max_power_watts: 1500, max_current_amps: 10, electricity_rate_per_kwh: 8 });

  const chartData = useMemo(() => [...readings].reverse().slice(-20), [readings]);
  const maxChartPower = Math.max(1, ...chartData.map(r => Number(r.power || 0)));

  async function refresh() {
    setLoading(true);
    try {
      const [l, s, r, t] = await Promise.all([
        api('/api/latest'),
        api('/api/summary'),
        api('/api/readings?limit=30'),
        api('/api/thresholds'),
      ]);
      setLatest(l.reading);
      setSummary(s);
      setReadings(r.readings || []);
      setThresholds(t.thresholds || thresholds);
      setMessage('Dashboard updated successfully');
    } catch (err) {
      setMessage(`Backend connection error: ${err.message}. Make sure FastAPI is running on ${API_BASE}`);
    } finally {
      setLoading(false);
    }
  }

  async function simulate(mode) {
    setLoading(true);
    try {
      await api(`/api/simulate?mode=${mode}`, { method: 'POST' });
      setMessage(`${mode} energy reading generated`);
      await refresh();
    } catch (err) { setMessage(err.message); }
    finally { setLoading(false); }
  }

  async function addManual(e) {
    e.preventDefault();
    setLoading(true);
    try {
      await api('/api/readings', { method: 'POST', body: JSON.stringify({
        appliance: manual.appliance,
        voltage: Number(manual.voltage),
        current: Number(manual.current),
        duration_minutes: Number(manual.duration_minutes),
      }) });
      setMessage('Manual reading saved');
      await refresh();
    } catch (err) { setMessage(err.message); }
    finally { setLoading(false); }
  }

  async function saveThresholds(e) {
    e.preventDefault();
    setLoading(true);
    try {
      await api('/api/thresholds', { method: 'PUT', body: JSON.stringify({
        max_power_watts: Number(thresholds.max_power_watts),
        max_current_amps: Number(thresholds.max_current_amps),
        electricity_rate_per_kwh: Number(thresholds.electricity_rate_per_kwh),
      }) });
      setMessage('Thresholds updated');
      await refresh();
    } catch (err) { setMessage(err.message); }
    finally { setLoading(false); }
  }

  async function relay(status) {
    setLoading(true);
    try {
      await api('/api/relay', { method: 'POST', body: JSON.stringify({ status }) });
      setMessage(`Relay turned ${status}`);
      await refresh();
    } catch (err) { setMessage(err.message); }
    finally { setLoading(false); }
  }

  async function clearData() {
    const ok = window.confirm('Delete all logged energy readings?');
    if (!ok) return;
    setLoading(true);
    try {
      await api('/api/clear', { method: 'POST' });
      setMessage('All readings cleared');
      await refresh();
    } catch (err) { setMessage(err.message); }
    finally { setLoading(false); }
  }

  useEffect(() => {
    refresh();
    const id = setInterval(refresh, 7000);
    return () => clearInterval(id);
  }, []);

  return (
    <main>
      <section className="hero">
        <div>
          <p className="eyebrow">IoT Course Project</p>
          <h1>Smart Home Energy Monitoring System</h1>
          <p className="subtitle">Monitor voltage, current, power, energy usage, estimated electricity cost and overload alerts in real time.</p>
        </div>
        <button className="primary" onClick={refresh} disabled={loading}><RefreshCw size={18}/> Refresh</button>
      </section>

      {message && <div className="notice">{message}</div>}

      <section className="grid cards">
        <Card title="Voltage" value={fmt(latest?.voltage)} unit=" V" icon={Zap} />
        <Card title="Current" value={fmt(latest?.current)} unit=" A" icon={Activity} />
        <Card title="Power" value={fmt(latest?.power)} unit=" W" icon={Gauge} tone={latest?.alert_status !== 'NORMAL' ? 'danger' : ''} />
        <Card title="Energy" value={fmt(latest?.energy_kwh, 4)} unit=" kWh" icon={BatteryCharging} />
        <Card title="Cost" value={fmt(latest?.estimated_cost)} unit=" ₹" icon={IndianRupee} />
        <Card title="Alerts" value={summary?.alert_count ?? 0} unit="" icon={AlertTriangle} tone={(summary?.alert_count || 0) > 0 ? 'danger' : ''} />
      </section>

      <section className="panel statusPanel">
        <div>
          <h2>Latest Status</h2>
          <p><b>Appliance:</b> {latest?.appliance || 'Main Circuit'}</p>
          <p><b>Alert:</b> <span className={latest?.alert_status === 'NORMAL' ? 'ok' : 'bad'}>{latest?.alert_status || 'NORMAL'}</span></p>
          <p><b>Relay:</b> {summary?.relay_status || 'OFF'}</p>
          <p><b>Total Energy:</b> {fmt(summary?.total_energy_kwh, 4)} kWh</p>
          <p><b>Total Cost:</b> ₹{fmt(summary?.estimated_total_cost)}</p>
        </div>
        <div className="actions">
          <button onClick={() => relay('ON')}><Power size={18}/> Relay ON</button>
          <button onClick={() => relay('OFF')}><Power size={18}/> Relay OFF</button>
          <a className="buttonLink" href={`${API_BASE}/api/export/csv`}><Download size={18}/> CSV</a>
          <a className="buttonLink" href={`${API_BASE}/api/export/pdf`}><Download size={18}/> PDF</a>
          <button className="dangerBtn" onClick={clearData}><Trash2 size={18}/> Clear Logs</button>
        </div>
      </section>

      <section className="grid two">
        <div className="panel">
          <h2>Generate Simulation</h2>
          <p className="muted">Use this if you do not have real ESP32/current sensor hardware.</p>
          <div className="simButtons">
            {['normal','high','overload','low_voltage','standby'].map(mode => (
              <button key={mode} onClick={() => simulate(mode)}>{mode.replace('_',' ')}</button>
            ))}
          </div>
        </div>

        <form className="panel form" onSubmit={addManual}>
          <h2>Manual Reading</h2>
          <label>Appliance / Circuit<input value={manual.appliance} onChange={e => setManual({...manual, appliance: e.target.value})}/></label>
          <label>Voltage<input type="number" value={manual.voltage} onChange={e => setManual({...manual, voltage: e.target.value})}/></label>
          <label>Current<input type="number" step="0.01" value={manual.current} onChange={e => setManual({...manual, current: e.target.value})}/></label>
          <label>Duration Minutes<input type="number" step="0.1" value={manual.duration_minutes} onChange={e => setManual({...manual, duration_minutes: e.target.value})}/></label>
          <button className="primary" type="submit"><Database size={18}/> Save Reading</button>
        </form>
      </section>

      <section className="grid two">
        <form className="panel form" onSubmit={saveThresholds}>
          <h2>Threshold Settings</h2>
          <label>Max Power Watts<input type="number" value={thresholds.max_power_watts} onChange={e => setThresholds({...thresholds, max_power_watts: e.target.value})}/></label>
          <label>Max Current Amps<input type="number" step="0.1" value={thresholds.max_current_amps} onChange={e => setThresholds({...thresholds, max_current_amps: e.target.value})}/></label>
          <label>Electricity Rate ₹/kWh<input type="number" step="0.1" value={thresholds.electricity_rate_per_kwh} onChange={e => setThresholds({...thresholds, electricity_rate_per_kwh: e.target.value})}/></label>
          <button className="primary" type="submit"><PlugZap size={18}/> Save Thresholds</button>
        </form>

        <div className="panel">
          <h2>Power Trend</h2>
          <div className="chart">
            {chartData.length === 0 ? <p className="muted">No readings yet</p> : chartData.map((r, idx) => (
              <div key={idx} className="barWrap" title={`${r.appliance}: ${fmt(r.power)} W`}>
                <div className={`bar ${r.alert_status !== 'NORMAL' ? 'barDanger' : ''}`} style={{ height: `${Math.max(8, (Number(r.power || 0) / maxChartPower) * 150)}px` }} />
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="panel">
        <h2>Recent Energy Logs</h2>
        <div className="tableWrap">
          <table>
            <thead>
              <tr><th>Time</th><th>Appliance</th><th>Voltage</th><th>Current</th><th>Power</th><th>Energy</th><th>Cost</th><th>Alert</th></tr>
            </thead>
            <tbody>
              {readings.map(r => (
                <tr key={r.id}>
                  <td>{r.timestamp}</td><td>{r.appliance}</td><td>{fmt(r.voltage)} V</td><td>{fmt(r.current)} A</td><td>{fmt(r.power)} W</td><td>{fmt(r.energy_kwh,4)}</td><td>₹{fmt(r.estimated_cost)}</td><td><span className={r.alert_status === 'NORMAL' ? 'ok' : 'bad'}>{r.alert_status}</span></td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>
    </main>
  );
}

createRoot(document.getElementById('root')).render(<App />);
