import { Route, Routes } from "react-router-dom";

import DashboardPage from "../pages/dashboard/DashboardPage";
import LoginPage from "../pages/auth/LoginPage";
import RegisterPage from "../pages/auth/RegisterPage";
import ProtectedRoute from "./ProtectedRoute";

export default function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<LoginPage />} />

      <Route path="/register" element={<RegisterPage />} />

      <Route
        path="/dashboard"
        element={
          <ProtectedRoute>
            <DashboardPage />
          </ProtectedRoute>
        }
      />
    </Routes>
  );
}