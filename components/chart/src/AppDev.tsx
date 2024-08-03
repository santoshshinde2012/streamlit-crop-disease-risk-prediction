import { PlotlyChart } from "./components/plotly";

const ActionComponent: React.FC = () => {
  const temperature = [20];
  const humidity = [60];
  const soilMoisture = [10];
  const riskPrediction = ["high"];
  return (
    <PlotlyChart
      temperature={temperature}
      humidity={humidity}
      soilMoisture={soilMoisture}
      riskPrediction={riskPrediction}
    ></PlotlyChart>
  );
};

export default ActionComponent;
