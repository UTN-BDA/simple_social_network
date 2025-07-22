function Publicacion({ publicacion }) {
  const { texto, fecha, imagen, imagenes, usuario } = publicacion;

  // Soportar tanto imagen única como lista de imágenes
  const fotos = imagenes || imagen || [];

  return (
    <div className="publicacion">
      <p><strong>{usuario}</strong> </p>
      <p>{fecha}</p>

      {texto && <p>{texto}</p>}

      {fotos.length > 0 && (
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: '10px', marginTop: 10 }}>
          {fotos.slice(0, 4).map((img, index) => (
            <img
              key={index}
              src={img}
              alt={`imagen ${index + 1}`}
            />
          ))}
        </div>
      )}
    </div>
  );
}

export default Publicacion;