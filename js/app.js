const KEY='vityarthi_tasks';
let tasks=JSON.parse(localStorage.getItem(KEY)||'[]');  

const $=id=>document.getElementById(id);
function save(){localStorage.setItem(KEY,JSON.stringify(tasks));render();}
function resetForm(){$('taskForm').reset();$('taskId').value='';$('cancel').style.display='none';}

function render(){
 const filter=$('filter').value;
 const shown=tasks.filter(t=>filter==='all'||(filter==='completed'?t.completed:!t.completed));
 $('total').textContent=tasks.length;
 $('pending').textContent=tasks.filter(t=>!t.completed).length;
 $('completed').textContent=tasks.filter(t=>t.completed).length;
 $('taskList').innerHTML=shown.length?shown.map(t=>`
 <article class="task ${t.completed?'done':''}">
  <div><h3>${escapeHtml(t.title)}</h3>
  <p><b>Subject:</b> ${escapeHtml(t.subject)} | <b>Deadline:</b> ${t.deadline} | <b>Priority:</b> <span class="${t.priority==='High'?'high':''}">${t.priority}</span></p></div>
  <div class="actions">
   <button onclick="toggleTask('${t.id}')">${t.completed?'Undo':'Complete'}</button>
   <button onclick="editTask('${t.id}')">Edit</button>
   <button onclick="deleteTask('${t.id}')">Delete</button>
  </div>
 </article>`).join(''):'<div class="empty">No tasks found.</div>';
}
function escapeHtml(s){return s.replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[c]));}
$('taskForm').addEventListener('submit',e=>{
 e.preventDefault();
 const id=$('taskId').value;
 const data={title:$('title').value.trim(),subject:$('subject').value.trim(),deadline:$('deadline').value,priority:$('priority').value};
 if(id){const t=tasks.find(x=>x.id===id);Object.assign(t,data)}
 else tasks.push({...data,id:crypto.randomUUID(),completed:false});
 save();resetForm();
});
function toggleTask(id){const t=tasks.find(x=>x.id===id);t.completed=!t.completed;save();}
function deleteTask(id){if(confirm('Delete this task?')){tasks=tasks.filter(x=>x.id!==id);save();}}
function editTask(id){const t=tasks.find(x=>x.id===id);$('taskId').value=t.id;$('title').value=t.title;$('subject').value=t.subject;$('deadline').value=t.deadline;$('priority').value=t.priority;$('cancel').style.display='inline-block';scrollTo(0,0)}
$('cancel').onclick=resetForm;$('filter').onchange=render;resetForm();render();
