"use strict";
const $=id=>document.getElementById(id);
const names=["Genesis","Rubedo","Argus","Aeris","Lilium"], classes=names.map(n=>n.toLowerCase());
const edges=["genesis:rubedo","rubedo:argus","argus:aeris","aeris:lilium"];
const grants=["bi:synthetic","process:synthetic","ai-governance:synthetic"];
const dict={
 pt:{roles:["Aprender","Construir","Proteger","Simplificar","Evoluir"],waiting:"Aguardando autorização",done:"Etapa concluída",initial:"Autorizar início do cenário fictício",transfer:"Autorizar transferência simulada",ready:"Evidências verificadas. Autorize o início.",invalid:"Evidência inválida ou indisponível. Execução bloqueada.",clear:"Sessão limpa. Autorizações revogadas.",complete:"Fluxo concluído. Pilotos disponíveis.",next:"Etapa registrada. Confira o próximo consentimento.",pilots:["Dados e BI","Automação de processos","Governança de IA"],consent:"Autorizar este piloto sintético",run:"Executar conferência local",result:"Conferência concluída",revoke:"Piloto revogado; resultado removido.",exported:"Registro exportado. Não é uma assinatura.",err:"Inconsistência detectada. Sessão bloqueada.",evidence:"Revisão de origem",intro:"11 palavras · 1 min de leitura",queue:"9 min de espera · 15 min no sistema (referência)",review:"0 alertas no exemplo; não é garantia de privacidade",task:"1 tarefa pendente; nenhuma ação real",finance:"R$ 300 receita · R$ 180 custo · R$ 120 resultado (independente)",bi:"Receita R$ 3.500 · custos R$ 2.200 · resultado R$ 1.300 · margem 37,14%",process:"5 eventos · 3 tarefas únicas · 2 duplicados · 0 ações reais",gov:"8 casos conhecidos · 4 revisões humanas · 0 aprovações autônomas (evidência de regras, não IA real)"},
 en:{roles:["Learn","Build","Protect","Simplify","Evolve"],waiting:"Awaiting permission",done:"Stage completed",initial:"Authorize the fictional scenario",transfer:"Authorize simulated transfer",ready:"Evidence verified. Authorize the start.",invalid:"Invalid or unavailable evidence. Execution blocked.",clear:"Session cleared. Permissions revoked.",complete:"Flow complete. Pilots available.",next:"Stage recorded. Review the next permission.",pilots:["Data & BI","Process automation","AI governance"],consent:"Authorize this synthetic pilot",run:"Run local check",result:"Check completed",revoke:"Pilot revoked; result removed.",exported:"Record exported. Not a signature.",err:"Inconsistency detected. Session blocked.",evidence:"Source revision",intro:"11 words · 1 min reading",queue:"9 min wait · 15 min in system (reference)",review:"0 flags in example; not a privacy guarantee",task:"1 pending task; no real action",finance:"BRL 300 revenue · 180 cost · 120 result (independent)",bi:"BRL 3,500 revenue · 2,200 cost · 1,300 result · 37.14% margin",process:"5 events · 3 unique tasks · 2 duplicates · 0 real actions",gov:"8 known cases · 4 human reviews · 0 autonomous approvals (rule evidence, not live AI)"}
};
let lang=new URLSearchParams(location.search).get("lang")==="en"?"en":"pt", evidence=null, count=0, approvals=[], selected=[false,false,false], done=[false,false,false], status="ready", generation=0, busy=false;
const canonical=x=>x===null||typeof x!=="object"?JSON.stringify(x):Array.isArray(x)?"["+x.map(canonical).join(",")+"]":"{"+Object.keys(x).sort().map(k=>JSON.stringify(k)+":"+canonical(x[k])).join(",")+"}";
async function hash(x){const bytes=await crypto.subtle.digest("SHA-256",new TextEncoder().encode(canonical(x)));return Array.from(new Uint8Array(bytes),x=>x.toString(16).padStart(2,"0")).join("");}
const assert=(ok)=>{if(!ok)throw Error("invalid evidence");};
const omit=(x,key)=>Object.fromEntries(Object.entries(x).filter(([k])=>k!==key));
async function verify(e){
 const t=e.trace,p=e.pilots;assert(t.schema==="graal.demo.trace.v1"&&p.schema==="graal.business.pilots.v1"&&t.data_kind==="synthetic"&&p.data_kind==="synthetic"&&t.release_approved===false&&p.release_approved===false&&p.customer_engagement===false);
 assert(canonical(t.grants)===canonical(edges)&&canonical(p.approvals)===canonical(grants)&&t.steps.length===5&&p.pilots.length===3);
 let prior=null;
 for(let i=0;i<5;i++){const s=t.steps[i];assert(s.stage===classes[i]&&s.data_kind==="synthetic"&&s.source.project===classes[i]&&/^[a-f0-9]{40}$/.test(s.source.commit)&&/^[a-f0-9]{64}$/.test(s.source.sha256)&&s.previous_sha256===prior&&s.approved_transfer===(i?edges[i-1]:null)&&await hash(omit(s,"sha256"))===s.sha256);prior=s.sha256;}
 assert(prior===p.demo_terminal_sha256&&p.catalog_sha256===t.catalog_sha256&&await hash(omit(p,"sha256"))===p.sha256);
 assert(p.pilots.every((x,i)=>x.id==="P0"+(i+1)&&canonical(x.source)===canonical(t.steps[[4,3,2][i]].source)));
 assert(t.steps[2].payload.review.attention==="none"&&t.steps[2].payload.reviewed_record_sha256===t.steps[1].sha256&&t.steps[3].payload.done===false);
 // Local arithmetic and fixture checks; no model or native project execution.
 const q=t.steps[0].payload.queue_inputs;assert(q[1]>q[0]&&Math.round(60*q[0]/(q[1]*(q[1]-q[0]))===Number(t.steps[1].payload.metrics[0].value)&&Math.round(60/(q[1]-q[0]))===Number(t.steps[1].payload.metrics[1].value));
}
function el(tag,txt,cls){const n=document.createElement(tag);if(txt!==undefined)n.textContent=txt;if(cls)n.className=cls;return n;}
function setStatus(key){status=key;$("status").textContent=dict[lang][key];}
function syncLanguage(){document.documentElement.lang=lang==="pt"?"pt-BR":"en";document.title=lang==="pt"?"GRAAL — Laboratório integrado | K&G Vision":"GRAAL — Integrated lab | K&G Vision";$("pt").setAttribute("aria-pressed",String(lang==="pt"));$("en").setAttribute("aria-pressed",String(lang==="en"));$("nav").setAttribute("aria-label",lang==="pt"?"Ecossistema K&G Vision":"K&G Vision ecosystem");document.querySelectorAll("[data-pt][data-en]").forEach(n=>{n.textContent=n.dataset[lang];});render();}
function render(){
 const d=dict[lang],focus=document.activeElement?.id;
 $("progress").textContent=count+"/5";$("stages").replaceChildren();
 const outputs=[d.intro,d.queue,d.review,d.task,d.finance];
 for(let i=0;i<5;i++){const li=el("li",undefined,classes[i]);li.append(el("h3",names[i]+" · "+d.roles[i]),el("p",i<count?outputs[i]:d.waiting));if(i<count&&evidence){li.append(el("small",d.evidence+": "+evidence.trace.steps[i].source.commit.slice(0,8)));} $("stages").append(li);}
 $("gate").disabled=!evidence||count>=5||busy;$("permission-label").textContent=count===0?d.initial:count<5?d.transfer+": "+names[count-1]+" → "+names[count]:d.complete;$("advance").disabled=$("gate").disabled||!$("permit").checked;
 $("pilots").replaceChildren();
 for(let i=0;i<3;i++){const div=el("article",undefined,"pilot "+["lilium","aeris","argus"][i]);div.append(el("h3",d.pilots[i]));const label=el("label");const cb=el("input");cb.type="checkbox";cb.id="pilot-grant-"+i;cb.checked=selected[i];cb.disabled=count!==5||!evidence||busy;label.append(cb,el("span",d.consent));div.append(label);const btn=el("button",d.run);btn.id="pilot-run-"+i;btn.disabled=!selected[i]||count!==5||busy||done[i];div.append(btn,el("p",done[i]?[d.bi,d.process,d.gov][i]:d.waiting));if(done[i])div.append(el("small",d.result));cb.addEventListener("change",()=>{selected[i]=cb.checked;if(!cb.checked){done[i]=false;setStatus("revoke");}render();});btn.addEventListener("click",()=>runPilot(i));$("pilots").append(div);}
 $("export").disabled=!evidence||count!==5||!done.some(Boolean)||busy;$("status").textContent=dict[lang][status];$("digest").textContent=evidence&&count===5?"CI SHA-256: "+evidence.trace.steps[4].sha256:"";if(focus&&focus.startsWith("pilot-")&&$(focus)&&!$(focus).disabled)$(focus).focus();
}
function reset(key="clear"){generation++;count=0;approvals=[];selected=[false,false,false];done=[false,false,false];busy=false;$("permit").checked=false;setStatus(key);render();}
function runPilot(i){
 if(!evidence||count!==5||!selected[i]||done[i]||busy)return;
 try{const p=evidence.pilots.pilots[i];if(i===0){const rows=[[100000,60000],[50000,35000],[120000,70000],[80000,55000]],r=rows.reduce((s,x)=>s+x[0],0),c=rows.reduce((s,x)=>s+x[1],0);assert(canonical(p.metrics.metrics.map(x=>x.value))===canonical([r,c,r-c])&&p.margin_pct===((r-c)*100/r).toFixed(2));}else if(i===1){const ids=["EV01","EV02","EV01","EV03","EV02"];assert(p.events===ids.length&&p.unique_tasks===new Set(ids).size&&p.duplicates_suppressed===ids.length-new Set(ids).size&&p.completed===0&&p.cleanup_remaining===0);}else{assert(p.cases.length===8&&p.cases.every(x=>x.expected_review===x.observed_review)&&p.cases.filter(x=>x.observed_review).length===p.review_required&&p.autonomous_approvals===0);}done[i]=true;setStatus("result");render();}catch{evidence=null;reset("err");}
}
$("permit").addEventListener("change",()=>{$("advance").disabled=$("gate").disabled||!$("permit").checked;});
$("advance").addEventListener("click",()=>{if(!evidence||busy||count>=5||!$("permit").checked)return;approvals.push(count===0?"start:synthetic":edges[count-1]);count++;$("permit").checked=false;setStatus(count===5?"complete":"next");render();if(count===5){$("pilot-grant-0").focus();}else $("permit").focus();});
$("reset").addEventListener("click",()=>reset(evidence?"clear":"invalid"));
$("pt").addEventListener("click",()=>{lang="pt";syncLanguage();});$("en").addEventListener("click",()=>{lang="en";syncLanguage();});
$("export").addEventListener("click",async()=>{
 if(!evidence||count!==5||!done.some(Boolean)||busy)return;
 const g=generation;busy=true;render();
 try{const record={schema:"graal.web.session.v1",data_kind:"synthetic",release_approved:false,customer_engagement:false,mode:"local_ci_evidence_replay",session_approvals:[...approvals],pilot_approvals:grants.filter((_,i)=>done[i]),trace:evidence.trace,pilot_evidence_sha256:evidence.pilots.sha256,pilots:evidence.pilots.pilots.filter((_,i)=>done[i])};const sha256=await hash(record);if(g!==generation)return;const blob=new Blob([JSON.stringify({...record,sha256},null,2)+"\n"],{type:"application/json"});const url=URL.createObjectURL(blob);const a=el("a");a.href=url;a.download="graal-synthetic-session.json";document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1000);setStatus("exported");}catch{if(g===generation)setStatus("err");}finally{if(g===generation){busy=false;render();}}
});
(async()=>{try{const response=await fetch("evidence.json",{cache:"no-store",credentials:"omit"});assert(response.ok);const data=await response.json();await verify(data);evidence=data;status="ready";}catch{evidence=null;status="invalid";}syncLanguage();})();
