import api from "../api/api";

export const register = (data) =>
  api.post("/auth/register", data);

export const login = (data) =>
  api.post("/auth/login", data);

export const getProfile = () =>
  api.get("/auth/me");