import axios from "axios";

const instance = axios.create({
  baseURL: "http://localhost:9009",
});

export default instance;
