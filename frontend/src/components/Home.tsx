"use client";
import { useState } from "react";

export default function Home() {
  const [topic, setTopic] = useState("");
  const [summary, setSummary] = useState("");
  const [content, setContent] = useState("");
  const [images, setImages] = useState<string[]>([]);
  const [feedback, setFeedback] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleGenerate = async () => {
    if (!topic.trim()) return;
    setLoading(true);
    setSummary("");
    setContent("");
    setImages([]);
    setFeedback([]);
    setError("");

    try {
      // STEP 1: ResearchAgent
      const res1 = await fetch(
        `http://localhost:8000/api/research?topic=${encodeURIComponent(topic)}`
      );
      if (!res1.ok) throw new Error("Failed to fetch summary");
      const data1 = await res1.json();
      setSummary(data1.summary);

      // STEP 2: WriterAgent
      const res2 = await fetch("http://localhost:8000/api/write", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ topic, context: data1.summary }),
      });
      if (!res2.ok) throw new Error("Failed to generate content");
      const data2 = await res2.json();
      setContent(data2.content);

      // STEP 3: ReviewerAgent
      const res4 = await fetch("http://localhost:8000/api/review", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ content: data2.content }),
      });
      if (!res4.ok) throw new Error("Failed to get feedback");
      const data4 = await res4.json();
      setFeedback(data4.feedback || []);

      // STEP 4: DesignerAgent
      const res3 = await fetch(
        `http://localhost:8000/api/images?topic=${encodeURIComponent(topic)}`
      );
      if (!res3.ok) throw new Error("Failed to fetch images");
      const data3 = await res3.json();
      setImages(data3.images || []);
    } catch (err: any) {
      setError(err.message || "An error occurred");
    }

    setLoading(false);
  };

  return (
    <main className="flex flex-col items-center justify-start min-h-screen p-6 bg-gray-50">
      <h1 className="text-3xl font-bold mb-6 text-gray-900">
        CAN BALKAC Studio
      </h1>

      <div className="flex gap-2 mb-6">
        <input
          type="text"
          placeholder="Enter a topic..."
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
          className="px-4 py-2 border rounded w-80 text-black"
        />
        <button
          onClick={handleGenerate}
          disabled={loading}
          className="px-6 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
        >
          {loading ? "Generating..." : "Generate"}
        </button>
      </div>

      {error && <div className="text-red-600 mb-4 font-semibold">{error}</div>}

      {summary && (
        <div className="w-full max-w-2xl bg-white p-4 rounded shadow mb-6">
          <h2 className="text-xl font-semibold mb-2 text-black">
            🔍 Research Summary
          </h2>
          <p className="text-gray-800">{summary}</p>
        </div>
      )}

      {content && (
        <div className="w-full max-w-2xl bg-white p-4 rounded shadow mb-6">
          <h2 className="text-xl font-semibold mb-2 text-black">
            📝 Generated Article
          </h2>
          <div className="prose max-w-none text-gray-800 whitespace-pre-wrap">
            {content}
          </div>
        </div>
      )}

      {feedback.length > 0 && (
        <div className="w-full max-w-2xl bg-white p-4 rounded shadow mb-6">
          <h2 className="text-xl font-semibold mb-2 text-black">
            🧠 Reviewer Feedback
          </h2>
          <ul className="list-disc list-inside text-gray-700">
            {feedback.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>
        </div>
      )}

      {images.length > 0 && (
        <div className="w-full max-w-5xl bg-white p-4 rounded shadow">
          <h2 className="text-xl font-semibold mb-2">🎨 Suggested Images</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {images.map((img, i) => (
              <img
                key={i}
                src={img}
                alt={`Generated ${i}`}
                className="w-full h-auto rounded border"
              />
            ))}
          </div>
        </div>
      )}
    </main>
  );
}
