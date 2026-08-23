fetch('/api/mandi').then(r=>r.json()).then(data=>{
  let div=document.getElementById('mandi-list');
  div.innerHTML=data.map(m=>`<div style="background:white;margin:10px;padding:10px;border-radius:8px">${m.crop} - Rs.${m.price} at ${m.market}</div>`).join('');
});