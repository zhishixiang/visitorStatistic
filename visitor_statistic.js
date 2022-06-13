//github:zhishixiang
var id = document.getElementById("visitorId");
var sum = document.getElementById("sum")

if(document.cookie.indexOf("uuid=") == -1)
{
	document.cookie = "uuid="+Math.random();
}

function getCookie(cname)
{
  var name = cname + "=";
  var ca = document.cookie.split(';');
  for(var i=0; i<ca.length; i++) 
  {
    var c = ca[i].trim();
    if (c.indexOf(name)==0) return c.substring(name.length,c.length);
  }
  return "";
}

function getVisitorData(uuid,domain)
{
	const xhr = new XMLHttpRequest();
	xhr.open("GET","https://st.api.bnnet.com.cn/release/getVisitorData?&uuid="+getCookie("uuid")+"&domain="+domain);
	xhr.send();
	xhr.onreadystatechange = function(){
		if(xhr.readyState == 4){
			if(xhr.status == 200){
				console.log("200 OK");
				id.innerText = xhr.response
			}
		}
	}
}
function getWebsiteData(domain)
{
	const xhr = new XMLHttpRequest();
	xhr.open("GET","https://st.api.bnnet.com.cn/release/getWebsiteData?&domain="+domain);
	xhr.send();
	xhr.onreadystatechange = function(){
		if(xhr.readyState == 4){
			if(xhr.status == 200){
				console.log("200 OK");
				sum.innerText = xhr.response
			}
		}
	}
}
console.log(getCookie("uuid"));
console.log(document.domain);
getVisitorData(getCookie("uuid"),document.domain);
getWebsiteData(document.domain);