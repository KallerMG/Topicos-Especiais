import React from "react";
import Select from "react-select";
import { useForm, Controller } from "react-hook-form";
import Input from "@material-ui/core/Input";
import { TextField, Checkbox, FormControlLabel } from "@material-ui/core";

import axios from "axios";

import { useState } from "react";

import "style.css";

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

const Busca = () => {
  const { control, handleSubmit } = useForm();
  const [data, setData] = useState([]);

  const onSubmit = (dados) => {
    try {
      setData([{ name: "inicio", CPU_Uso: 0 }]);
      const chegada = axios
        .post("http://127.0.0.1:5000/busca", dados)
        .then((response) => {
          setData(response.data);
        });
      console.log(dados);
      console.log(data);
    } catch (error) {
      console.log("erro na coneção");
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit(onSubmit)}>
        <Controller
          name="valor_informado"
          control={control}
          defaultValue=""
          rules={{ required: true }}
          render={({ field }) => <Input {...field} />}
        />
        <Controller
          name="busca"
          control={control}
          render={({ field }) => (
            <Select
              {...field}
              options={[
                { value: "memoBaixa", label: "Memoria <= 'x'" },
                {
                  value: "tempMaxMin",
                  label: "Temperatura Maxima e Minima em 'x' dias ",
                },
              ]}
            />
          )}
        />
        <label>CPU Uso</label>
        <Controller
          name="CPU_Uso"
          control={control}
          defaultValue={false}
          render={({ field }) => <Checkbox {...field} label="name" />}
        />
        <label>CPU Freq</label>
        <Controller
          name="CPU_Freq"
          control={control}
          defaultValue={false}
          render={({ field }) => <Checkbox {...field} label="name" />}
        />
        <label>CPU Media</label>
        <Controller
          name="CPU_Media"
          control={control}
          defaultValue={false}
          render={({ field }) => <Checkbox {...field} label="name" />}
        />
        <label>CPU Temp</label>
        <Controller
          name="CPU_Temp"
          control={control}
          defaultValue={false}
          render={({ field }) => <Checkbox {...field} label="name" />}
        />
        <label>Memo Uso</label>
        <Controller
          name="Memo_Uso"
          control={control}
          defaultValue={false}
          render={({ field }) => <Checkbox {...field} label="name" />}
        />
        <label>Memo Disp</label>
        <Controller
          name="Memo_Disp"
          control={control}
          defaultValue={false}
          render={({ field }) => <Checkbox {...field} label="name" />}
        />
        <label>Memo Porc</label>
        <Controller
          name="Memo_Porc"
          control={control}
          defaultValue={false}
          render={({ field }) => <Checkbox {...field} label="name" />}
        />
        <input type="submit" />
      </form>

      <div className="testediv">
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

export default Busca;
