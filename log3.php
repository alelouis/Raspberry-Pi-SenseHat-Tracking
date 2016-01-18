<!DOCTYPE html>
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="style.css">
</head>
<script src="http://d3js.org/d3.v3.min.js"></script>
<script src="d3graph3.js"></script>
<body>
  <h1 style="margin-left:50px;">SenseHat Raspberry - Logs :
    <script>
      var d = new Date();
      var year = d.getFullYear();
      var month = ("0" + (d.getMonth() + 1)).slice(-2);
      var day = ("0" + (d.getDate())).slice(-2);
      var filename = day + "/" + month + "/" + year;
      document.write(filename);
    </script></br>
    <select id="files" onchange="createGraph()">
      <?php
      $dir    = '/var/www/html/sense/';
      $files1 = scandir($dir);
      foreach ($files1 as $value) {
          echo "<option>";
          print_r($value);
          echo "</option>";
      }
      ?>
    </select>
  </h1></br>
  <div id="graph">
  </div>
</body>
