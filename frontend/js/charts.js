fetch('/api/dashboard').then(r=>r.json()).then(d=>{
  document.getElementById('farmers').innerText=d.total_farmers;
  document.getElementById('jobs').innerText=d.total_jobs;
  new Chart(document.getElementById('myChart'),{type:'bar',data:{labels:['Farmers','Jobs','Crops'],datasets:[{label:'Count',data:d.chart_data,backgroundColor:'#2e7d32'}]}});
});