import React from "react";
import { Switch, Route } from "react-router-dom";
import Home from "./pages/Home";
import Busca from "./pages/Busca";

export default () => {
  return (
    <Switch>
      <Route exact path="/">
        <Home />
      </Route>
      <Route exact path="/busca">
        <Busca />
      </Route>
    </Switch>
  );
};
