import React, {useState} from 'react';
import {createRoot} from 'react-dom/client';
import {toggleTask, progress} from './tasks.js';
import './style.css';
function App() {
  const [tasks,setTasks] = useState([
    {id:1,title:'Inspect the repository',done:false},
    {id:2,title:'Make one small change',done:false},
    {id:3,title:'Run the tests',done:false},
    {id:4,title:'Review the diff',done:false}
  ]);
  const status=progress(tasks);
  return <main><p className="eyebrow">Termwise Atlas · React lab</p><h1>Practice with<br/>a purpose.</h1><p>Four small steps toward a change you understand.</p><section aria-label="Learning checklist"><p role="status">{status.completed} of {status.total} steps complete</p><progress aria-label="Learning progress" max="100" value={status.percent}/><ul>{tasks.map(task=><li key={task.id}><label><input type="checkbox" checked={task.done} onChange={()=>setTasks(current=>toggleTask(current,task.id))}/><span>{task.title}</span></label></li>)}</ul></section><p className="note">This exercise keeps state in memory. Reloading starts a fresh practice session.</p></main>;
}
createRoot(document.getElementById('root')).render(<React.StrictMode><App/></React.StrictMode>);
