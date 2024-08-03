import {
  withStreamlitConnection,
  Streamlit,
  ComponentProps,
} from "streamlit-component-lib";
import "./App.css";
import { useEffect, useState } from "react";
import { Button } from "./components/button";

const ActionComponent: React.FC<ComponentProps> = ({ args }) => {
  const [spec, setSpec] = useState({ name: "", location: "" });

  useEffect(() => {
    Streamlit.setFrameHeight();
    if (args.spec) {
      setSpec(JSON.parse(args.spec));
    }
  }, [args]);

  return <Button name={spec.name} location={spec.location}></Button>;
};

const StreamlitComponent = withStreamlitConnection(ActionComponent);

export default StreamlitComponent;
