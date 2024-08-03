import { PlotData } from "plotly.js";
import React, { useEffect } from "react";
import Plot from "react-plotly.js";
import { Streamlit } from "streamlit-component-lib";

interface IProps {
  cropName?: string;
  temperature: number[];
  humidity: number[];
  soilMoisture: number[];
  riskPrediction: string[];
}

const PlotlyChart: React.FC<IProps> = ({
  cropName,
  temperature,
  humidity,
  soilMoisture,
  riskPrediction,
}) => {
  const riskColors: { [key: string]: string } = {
    low: "green",
    medium: "gray",
    high: "red",
  };

  const colorMap = riskPrediction.map((risk) => riskColors[risk]);

  const data = {
    type: "scatter3d",
    mode: "markers",
    x: temperature,
    y: humidity,
    z: soilMoisture,
    hovertemplate: 
    'Temperature: %{x}°C<br>' +
    'Humidity: %{y}<br>' +
    'Soil Moisture: %{z}<br><extra></extra>',
    text: riskPrediction,
    marker: {
      size: 3,
      color: colorMap,
      colorscale: [
        [0, "green"],
        [0.5, "gray"],
        [1, "red"],
      ],
      cmin: 0,
      cmax: 2,
      colorbar: {
        tickvals: [0, 1, 2],
        ticktext: ["Low", "Medium", "High"],
      },
    },
  } as PlotData;

  useEffect(() => {
    Streamlit.setComponentValue('DONE');
  },[]);

  const layout = {
    title: `<span>Crop (<b>${cropName}</b>) Disease Risk Prediction is <b style="color:${riskColors[riskPrediction.toString()]};text-transform: capitalize;">${riskPrediction.toString()}</b><span>`,
    autosize: true,
    scene: {
      xaxis: { title: "Temperature (°C)" },
      yaxis: { title: "Humidity" },
      zaxis: { title: "Soil Moisture" },
    }
  };

  return <Plot data={[data]} layout={layout} />;
};

export { PlotlyChart };
