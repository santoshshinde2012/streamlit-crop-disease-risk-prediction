import { useState } from "react";
import { Streamlit } from "streamlit-component-lib";

interface IProps {
  name: string;
  location: string;
}
export const Button: React.FC<IProps> = ({ location }) => {
  const [count, setCount] = useState(1);

  const handleClick = () => {
    setCount((count) => count + 1);
    Streamlit.setComponentValue(count);
  };

  return (
    <div className="card">
      <button onClick={handleClick}>
        Click Me {location ? `- ${location}` : ""}
      </button>
    </div>
  );
};
