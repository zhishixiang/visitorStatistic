from flask import Flask, jsonify, render_template, request, url_for, make_response
import pymysql


app = Flask(__name__)

db = pymysql.connect()
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS access(domain TEXT,id TEXT,ip TEXT,ua TEXT,uuid TEXT)")
cursor.close()
@app.route("/getVisitorData")
def getVisitorData():
  #收集参数消息
  uuid = str(request.values.get('uuid'))
  domain = str(request.values.get('domain'))
  ip = str(request.headers["X-Forwarded-For"])
  ua = str(request.headers.get("User-Agent"))
  #查询结果
  cursor = db.cursor()
  isVisited = cursor.execute("SELECT uuid FROM access WHERE uuid=%s AND domain=%s",(uuid,domain))
  visitorNum = cursor.execute("SELECT domain FROM access WHERE domain=%s",domain)
  if "sqlmap" in ua:
    cursor.close()
    return "个人小项目，运营不易请体谅，感谢您的配合"
  elif "python" in ua:
    cursor.close()
    return "请使用/getWebsiteData接口查询网站数据数据库"
  elif "spider" in ua or "bot" in ua:
    cursor.close()
    return "机器人访问，不计入总数据"
  elif isVisited == 0:
    cursor.execute("INSERT INTO `access` (`domain`, `id`, `ip`, `ua`, `uuid`) VALUES (%s,%s,%s,%s,%s)",(domain,str(visitorNum+1),ip,ua,uuid))
    res = make_response(str(visitorNum+1))
  else:
    cursor.execute("SELECT id FROM access WHERE uuid=%s AND domain=%s",(uuid,domain))
    id = cursor.fetchone()[0]
    res = make_response(str(id))
  db.commit()
  cursor.close()
  #捏麻麻地跨域问题搞了我一个早上
  res.headers['Access-Control-Allow-Origin'] = "*"  
  res.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
  return res

@app.route("/getWebsiteData")
def getWebsiteData():
  domain = str(request.values.get('domain'))
  cursor = db.cursor()
  cursor.execute("SELECT COUNT(*) AS SUM FROM access WHERE domain=%s",domain)
  sum = cursor.fetchone()[0]
  res = make_response(str(sum))
  res.headers['Access-Control-Allow-Origin'] = "*"
  res.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
  return res

@app.route("/demo")
def demo():
  return render_template("demo.html")
# 启动服务，监听 9000 端口，监听地址为 0.0.0.0
app.run(port=9000, host='0.0.0.0')
