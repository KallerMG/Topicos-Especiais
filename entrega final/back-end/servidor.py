from flask import Flask,jsonify,request
from flask_cors import CORS
import json
import time
import sistema
import selectBanco

from threading import Thread


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
  busca= content["busca"]

  def f(x):
    return {
        'ultimoDia': selectBanco.ultimosDias(str(content["valor_informado"])),
        'memoBaixa': selectBanco.memoPorcBaixa(str(content["valor_informado"])),
        'usoDias': selectBanco.cpuUsoDias(str(content["valor_informado"])),
        'freqDias': selectBanco.cpuFreqDias(str(content["valor_informado"])),
        'tempDias': selectBanco.cpuTempDias(str(content["valor_informado"])),
    }.get(x, 9)    # 9 is default if x not found

  """ valores = [{'name': "data" ,'CPU_Uso' : 10000}] """

  valores = f(busca["value"])
  return jsonify(valores)


t = Thread(app.run())
t.start()




