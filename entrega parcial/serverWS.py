from flask import Flask,jsonify,request
from flask_cors import CORS
import time
import sistema
import selectBanco


app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
  data = str(time.strftime('%H:%M:%S', time.localtime()))
  cpu_uso = sistema.cpuUsoKaller()
  cpu_freq = sistema.cpuFreqKaller()
  cpu_media = sistema.cpuMediaKaller()
  cpu_temp = sistema.cpuTempKaller()
  memo_uso = sistema.memoUsoKaler()
  memo_disp = sistema.memoDispKaller()
  memo_porc = sistema.memoPorcentKaller()
  memo_livre = sistema.memoLivreKaller()
  fan_vel = sistema.fanVelKaller()    


  valores = [{'name': data ,'CPU_Uso' : cpu_uso, 'CPU_Freq': cpu_freq, 'CPU_Media': cpu_media, 'CPU_Temp': cpu_temp, 'Memoria_Uso' :memo_uso, 'Memoria_Disp' : memo_disp, 'Memoria_Porc' : memo_porc, 'Memoria_Livre': memo_livre }]
  return jsonify(valores)

@app.route('/busca', methods=['GET', 'POST'])
def busca():
  content = request.json
  print (content)

  """ valores = [{'name': "data" ,'CPU_Uso' : 10000}] """

  valores = selectBanco.memoPorcBaixa()
  return jsonify(valores)


app.run()