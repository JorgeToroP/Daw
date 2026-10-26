async function pedirCafe() {
  try {
    console.log("Pidiendo un cafe...");

    await new promise((resolve) => setTimeout(resolve, 2000));

    console.log("han pasado 2 segundos");
    console.log("Tu cafe esta listo");
  } catch (error) {
    console.log("error al pedir el cafe");
  }
}


pedirCafe();
