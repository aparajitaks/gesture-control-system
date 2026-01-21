import { useEffect } from "react";

export default function Camera() {
  useEffect(() => {
    const video = document.getElementById("video");

    navigator.mediaDevices.getUserMedia({ video: true }).then((stream) => {
      video.srcObject = stream;
    });
  }, []);

  return (
    <video
      id="video"
      autoPlay
      playsInline
      width="320"
      style={{ border: "2px solid black" }}
    />
  );
}
