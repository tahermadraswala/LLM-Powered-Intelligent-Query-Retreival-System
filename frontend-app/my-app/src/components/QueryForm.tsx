import React, { useState } from "react";

const API_URL = "http://127.0.0.1:5000/query";

const QueryForm: React.FC = () => {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setResponse("");
    try {
      const res = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query }),
      });
      const data = await res.json();
      setResponse(data.answer || "No answer received.");
    } catch {
      setResponse("Error connecting to backend.");
    }
    setLoading(false);
  };

  return (
    <div className="query-form">
      <form onSubmit={handleSubmit} action="#">
        <input
          type="text"
          value={query}
          onChange={e => setQuery(e.target.value)}
          placeholder="Type your insurance query..."
          required
        />
        <button type="submit" disabled={loading}>
          {loading ? "Processing..." : "Submit"}
        </button>
      </form>
      <div className="response">
        {response && (
          <>
            <strong>Response:</strong>
            <div style={{ whiteSpace: "pre-wrap", marginTop: "10px" }}>{response}</div>
          </>
        )}
      </div>
    </div>
  );
};

export default QueryForm;