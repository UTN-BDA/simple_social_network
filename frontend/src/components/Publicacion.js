function Publicacion({ publicacion }) {
  const { texto, fecha, imagen, imagenes } = publicacion;

  // Soportar tanto imagen única como lista de imágenes
  const fotos = imagenes || imagen || [];

  return (
    <div style={{ border: "1px solid gray", padding: 10, marginBottom: 10 }}>
      <p><strong>Fecha:</strong> {fecha}</p>

      {texto && <p>{texto}</p>}

      {fotos.length > 0 && (
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: '10px', marginTop: 10 }}>
          {fotos.slice(0, 4).map((img, index) => (
            <img
              key={index}
              src={img}
              alt={`imagen ${index + 1}`}
              style={{ width: '150px', height: 'auto', objectFit: 'cover', borderRadius: 5 }}
            />
          ))}
        </div>
      )}
    </div>
  );
}

export default Publicacion;