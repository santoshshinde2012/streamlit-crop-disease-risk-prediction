import {
  withStreamlitConnection,
  Streamlit,
  ComponentProps,
} from "streamlit-component-lib";
import { useEffect, useState } from "react";
import { PlotlyChart } from "./components/plotly";

const ActionComponent: React.FC<ComponentProps> = ({ args }) => {
  const [cropName, setCropName] = useState("");
  const [temperature, setTemperature] = useState<number[]>([]);
  const [humidity, setHumidity] = useState<number[]>([]);
  const [soilMoisture, setSoilMoisture] = useState<number[]>([]);
  const [riskPrediction, setRiskPrediction] = useState<string[]>([]);

  useEffect(() => {
    Streamlit.setFrameHeight();
    if (args.spec) {
      const {
        crop_name,
        temperature,
        humidity,
        soil_moisture,
        risk_prediction,
      } = JSON.parse(args.spec);
      setCropName(crop_name);
      setTemperature(temperature || []);
      setHumidity(humidity || []);
      setSoilMoisture(soil_moisture || []);
      setRiskPrediction(risk_prediction || []);
    }
  }, [args]);

  return (
    <PlotlyChart
      cropName={cropName}
      temperature={temperature}
      humidity={humidity}
      soilMoisture={soilMoisture}
      riskPrediction={riskPrediction}
    ></PlotlyChart>
  );
};

const StreamlitComponent = withStreamlitConnection(ActionComponent);

export default StreamlitComponent;
