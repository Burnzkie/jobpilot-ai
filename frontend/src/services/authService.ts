import api from "../api/axios";

export interface RegisterData {
  name: string;
  email: string;
  password: string;
}

export interface LoginData {
  email: string;
  password: string;
}

export const register = async (data: RegisterData) => {
  const response = await api.post("/api/auth/register", data);
  return response.data;
};

export const login = async (data: LoginData) => {
  const response = await api.post("/api/auth/login", data);
  return response.data;
};