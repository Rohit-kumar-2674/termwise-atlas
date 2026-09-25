export function toggleTask(tasks, id) {
  return tasks.map(task => task.id === id ? {...task, done: !task.done} : task);
}
export function progress(tasks) {
  const completed = tasks.filter(task => task.done).length;
  return {completed, total: tasks.length, percent: tasks.length ? Math.round(completed / tasks.length * 100) : 0};
}
