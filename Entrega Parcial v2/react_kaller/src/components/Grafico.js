import React from "react";

import {
  Line,
  LineChart,
  XAxis,
  YAxis,
  Tooltip,
  Label,
  AreaChart,
  linearGradient,
  Area,
  CartesianGrid,
  Legend,
} from "recharts";
import "style.css";

const Grafico = (
  texto = "ola sou um grafico",
  data2 = [],
  datakey = "CPU_Uso"
) => {
  console.log(data2);
  return (
    <div>
      <AreaChart
        width={500}
        height={300}
        data={data2}
        margin={{ top: 10, right: 30, left: 0, bottom: 0 }}
      >
        <defs>
          <linearGradient id="colorPv" x1="0" y1="0" x2="0" y2="1">
            <stop offset="90%" stopColor="#82ca9d" stopOpacity={1} />
            <stop offset="95%" stopColor="#82ca9d" stopOpacity={0} />
          </linearGradient>
        </defs>
        <XAxis dataKey="name" />
        <YAxis />
        <CartesianGrid strokeDasharray="3 3" />
        <Tooltip />
        <Legend verticalAlign="top" height={36} />
        <Area
          type="monotone"
          dataKey={datakey}
          stroke="#82ca9d"
          fillOpacity={1}
          fill="url(#colorPv)"
        />
      </AreaChart>
    </div>
  );
};

export default Grafico;
