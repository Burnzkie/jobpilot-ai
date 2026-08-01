import { useState } from "react";
import { useNavigate } from "react-router-dom";

import { login as loginService } from "../../services/authService";
import { useAuth } from "../../context/AuthContext";

export default function LoginPage() {
  const navigate = useNavigate();
  const { login } = useAuth();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async () => {
    try {
      const response = await loginService({
        email,
        password,
      });

      login(response.access_token);

      navigate("/dashboard");
    } catch (error) {
      alert("Invalid credentials");
    }
  };

  return (
    <div>
      <h1>Login</h1>

      <input
        placeholder="Email"
        onChange={(e) => setEmail(e.target.value)}
      />

      <input
        type="password"
        placeholder="Password"
        onChange={(e) => setPassword(e.target.value)}
      />

      <button onClick={handleSubmit}>
        Login
      </button>
    </div>
  );
}