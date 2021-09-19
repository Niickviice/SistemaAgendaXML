<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="html" />
  <xsl:template match="/agenda">
      <html>
      <head>
        <title>Agenda</title>
        <!-- estilos para las tablas -->
        <style type="text/css">
          body {
            background-color: blue;
            font-family: Arial;
          }
          #main-container{
            margin: 110px auto;
            width: 400px;
          }
          table {
            background-color: white;
            text-align: center;
            color: pink;
            border-style: dotted;
            width: 100%;
          }
          th, td{
            padding: 10px;
          }
          thead{
            border-bottom: solid 7px white;
            color: yellow;
          }
          tr:nth-child(even){
            background-color: #ddd;
          }
          tr:hover td{
            background-color: #4ab7d9;
          }
        </style>
      </head> 
      <body>
        <center>
          <h1>Contactos</h1>
        </center>
        <table>
          <tr bgcolor="#538ee0">
            <th>Nombre</th>
            <th>Apellido</th>
            <th>Telefono</th>
            <th>Celular</th>
            <th>Correo</th>
            <th>Codigo Postal</th>
            <th>Estado</th>
            <th>dirección</th>
          </tr>
          <xsl:for-each select="contacto">
            <tr>
              <td>
                <xsl:value-of select="nombre" />
              </td>
              <td>
                <xsl:value-of select="apellido" />
              </td>
              <td>
                <xsl:value-of select="telefono" />
              </td>
              <td>
                <xsl:value-of select="celular" />
              </td>
              <td>
                <xsl:value-of select="correo" />
              </td>
              <td>
                <xsl:value-of select="codigoPostal" />
              </td>
              <td>
                <xsl:value-of select="estado" />
              </td>
              <td>
                <xsl:value-of select="direccion" />
              </td>
            </tr>
          </xsl:for-each>
        </table>
        <hr />
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
