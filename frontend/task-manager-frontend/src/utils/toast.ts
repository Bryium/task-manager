import Toastify from "toastify-js";
import "toastify-js/src/toastify.css";

export const showToast = (
  message: string,
  type: "success" | "error" = "success"
) => {
  Toastify({
    text: message,
    duration: 3000,
    gravity: "top",
    position: "right",
    backgroundColor: type === "success" ? "#4CAF50" : "#f44336",
  }).showToast();
};
