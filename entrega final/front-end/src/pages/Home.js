import React from "react";

import { useEffect, useState, useRef } from "react";
import {
  XAxis,
  YAxis,
  Tooltip,
  AreaChart,
  Area,
  CartesianGrid,
  Legend,
  PieChart,
  Pie,
} from "recharts";
import axios from "axios";
import "style.css";

import Grafico from "../components/Grafico";

const Home = ({}) => {
  const [data, setData] = useState([]);

  const [timer, setTimer] = useState(3595);
  const increment = useRef(null);
  const increment2 = useRef(null);

  /* função ao montar */

  const iniGrafico = () => {
    try {
      increment2.current = setInterval(() => {
        const chegada = axios.get("http://127.0.0.1:5000/").then((response) => {
          setData((cpuPorcentagem) => [...cpuPorcentagem, response.data[0]]);
        });
      }, 2000);
    } catch (error) {
      console.log("erro na coneção");
    }
  };

  const useMountEffect = (fun) => useEffect(fun, []);
  useMountEffect(iniGrafico);

  return (
    <div>
      <h1 className="tituloHome">Monitor de Recursos</h1>
      <div className="graficodiv">
        <div>
          <h3 className="testeh3">CPU Uso</h3>
          <AreaChart
            width={500}
            height={300}
            data={data}
            margin={{ top: 10, right: 30, left: 0, bottom: 0 }}
          >
            <defs>
              <linearGradient id="colorUso" x1="0" y1="0" x2="0" y2="1">
                <stop offset="20%" stopColor="#FFF700" stopOpacity={1} />
                <stop offset="95%" stopColor="#FFF700" stopOpacity={0} />
              </linearGradient>
            </defs>
            <XAxis dataKey="name" />
            <YAxis />
            <CartesianGrid strokeDasharray="3 3" />
            <Tooltip />
            <Legend verticalAlign="top" height={36} />
            <Area
              type="monotone"
              dataKey="CPU_Uso"
              stroke="#FFF700"
              fillOpacity={1}
              fill="url(#colorUso)"
            />
          </AreaChart>
        </div>
        <div>
          <h3 className="testeh3">CPU Freq</h3>
          <AreaChart
            width={500}
            height={300}
            data={data}
            margin={{ top: 10, right: 30, left: 0, bottom: 0 }}
          >
            <defs>
              <linearGradient id="colorFreq" x1="0" y1="0" x2="0" y2="1">
                <stop offset="20%" stopColor="#DC00FF" stopOpacity={0.8} />
                <stop offset="95%" stopColor="#DC00FF" stopOpacity={0} />
              </linearGradient>
            </defs>
            <XAxis dataKey="name" />
            <YAxis />
            <CartesianGrid strokeDasharray="3 3" />
            <Tooltip />
            <Legend verticalAlign="top" height={36} />
            <Area
              type="monotone"
              dataKey="CPU_Freq"
              stroke="#DC00FF"
              fillOpacity={1}
              fill="url(#colorFreq)"
            />
          </AreaChart>
        </div>
        <div>
          <h3 className="testeh3">CPU Media</h3>
          <AreaChart
            width={500}
            height={300}
            data={data}
            margin={{ top: 10, right: 30, left: 0, bottom: 0 }}
          >
            <defs>
              <linearGradient id="colorMedia" x1="0" y1="0" x2="0" y2="1">
                <stop offset="20%" stopColor="#0FFF00" stopOpacity={1} />
                <stop offset="95%" stopColor="#0FFF00" stopOpacity={0} />
              </linearGradient>
            </defs>
            <XAxis dataKey="name" />
            <YAxis />
            <CartesianGrid strokeDasharray="3 3" />
            <Tooltip />
            <Legend verticalAlign="top" height={36} />
            <Area
              type="monotone"
              dataKey="CPU_Media"
              stroke="#0FFF00"
              fillOpacity={1}
              fill="url(#colorMedia)"
            />
          </AreaChart>
        </div>
        <div>
          <h3 className="testeh3">CPU Temp</h3>
          <AreaChart
            width={500}
            height={300}
            data={data}
            margin={{ top: 10, right: 30, left: 0, bottom: 0 }}
          >
            <defs>
              <linearGradient id="colorPv2" x1="0" y1="0" x2="0" y2="1">
                <stop offset="90%" stopColor="#FF4017" stopOpacity={0.6} />
                <stop offset="95%" stopColor="#FF4017" stopOpacity={0} />
              </linearGradient>
            </defs>
            <XAxis dataKey="name" />
            <YAxis />
            <CartesianGrid strokeDasharray="3 3" />
            <Tooltip />
            <Legend verticalAlign="top" height={36} />
            <Area
              type="monotone"
              dataKey="CPU_Temp"
              stroke="#FF4017"
              fillOpacity={1}
              fill="url(#colorPv2)"
            />
          </AreaChart>
        </div>
        <div>
          <h3 className="testeh3">Memoria Porc</h3>
          <AreaChart
            width={500}
            height={300}
            data={data}
            margin={{ top: 10, right: 30, left: 0, bottom: 0 }}
          >
            <defs>
              <linearGradient id="colorPv3" x1="0" y1="0" x2="0" y2="1">
                <stop offset="20%" stopColor="#8F00FF" stopOpacity={0.7} />
                <stop offset="95%" stopColor="#8F00FF" stopOpacity={0} />
              </linearGradient>
            </defs>
            <XAxis dataKey="name" />
            <YAxis />
            <CartesianGrid strokeDasharray="3 3" />
            <Tooltip />
            <Legend verticalAlign="top" height={36} />
            <Area
              type="monotone"
              dataKey="Memoria_Porc"
              stroke="#8F00FF"
              fillOpacity={1}
              fill="url(#colorPv3)"
            />
          </AreaChart>
        </div>

        <div>
          <h3 className="testeh3">Memoria Teste</h3>
          <AreaChart
            width={500}
            height={300}
            data={data}
            margin={{ top: 10, right: 30, left: 0, bottom: 0 }}
          >
            <defs>
              <linearGradient id="colorUso" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#FFB200" stopOpacity={0.7} />
                <stop offset="95%" stopColor="#FFB200" stopOpacity={0} />
              </linearGradient>
              <linearGradient id="colorDisp" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#C9FF00" stopOpacity={0.7} />
                <stop offset="95%" stopColor="#C9FF00" stopOpacity={0} />
              </linearGradient>
              <linearGradient id="colorLivre" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#003EFF" stopOpacity={0.7} />
                <stop offset="95%" stopColor="#003EFF" stopOpacity={0} />
              </linearGradient>
            </defs>
            <XAxis dataKey="name" />
            <YAxis />
            <CartesianGrid strokeDasharray="3 3" />
            <Tooltip />
            <Legend verticalAlign="top" height={36} />
            <Area
              type="monotone"
              dataKey="Memoria_Uso"
              stroke="#FFB200"
              fillOpacity={1}
              fill="url(#colorUso)"
            />
            <Area
              type="monotone"
              dataKey="Memoria_Disp"
              stroke="#C9FF00"
              fillOpacity={1}
              fill="url(#colorDisp)"
            />
            <Area
              type="monotone"
              dataKey="Memoria_Livre"
              stroke="#003EFF"
              fillOpacity={1}
              fill="url(#colorLivre)"
            />
          </AreaChart>
        </div>
      </div>
    </div>
  );
};

export default Home;
