import axios from "axios";
import { exit } from "process";

const apiService = () => {
  const baseURL = process.env.BACKEND_URL;

  if (!baseURL) {
    console.error("BACKEND_URL is not set");
    throw new Error("BACKEND_URL is not set", {
      cause: "BACKEND_URL is not set",
    });
  }

  console.log("baseURL", baseURL);

  return axios.create({
    baseURL: "http://localhost:3000",
    timeout: 10000,
    headers: {
      "Content-type": "application/json",
    },
  });
};

export default apiService;
