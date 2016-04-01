<!DOCTYPE html>
<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="css/pikaday.css">
  <link rel="stylesheet" href="css/skeleton.css">
  <link rel="stylesheet" href="css/normalize.css">
</head>
<script src="moment.js"></script>
<script src="pikaday.js"></script>
<script src="dygraph-combined-dev.js"></script>
<body>
  <h1 style="margin-left:50px;">SenseHat Raspberry - Last logs :
    <script>
      document.write(moment().format('MMMM Do YYYY'));
    </script>
  </h1>
  <input type="text" id="datepicker" onchange="createGraph()" placeholder="Select Date" style="margin-left:50px;"></br>
  <div id="graphTemp" style="width:500px; height:200px; margin-top:10px; display: inline-block;"></div>
  <div id="graphHumid" style="width:500px; height:200px;display: inline-block;"></div>
  <div id="graphPressure" style="width:500px; height:200px;display: inline-block;"></div>
  </div>
  <script>
  var picker = new Pikaday({
      field: document.getElementById('datepicker'),
      format: 'YYYY_MM_DD',
      onSelect: function() {
          console.log(this.getMoment().format('YYYY_MM_DD'));
      },
      minDate: new Date(2016, 3, 1),
      maxDate: new Date(),
      position: 'bottom left',
      reposition: false
  });

  function createGraph(){
    var filenameT = "./logs/" + picker.getMoment().format('DD_MM_YYYY') + "_temp.csv";
    var filenameH = "./logs/" + picker.getMoment().format('DD_MM_YYYY') + "_humidity.csv";
    var filenameP = "./logs/" + picker.getMoment().format('DD_MM_YYYY') + "_pressure.csv";
      var gt = new Dygraph(
            document.getElementById("graphTemp"), filenameT, {
            axisLabelFontSize : 10,
            axisLineColor : "rgb(20, 20, 20)",
            axisLabelColor : "rgb(20, 20, 20)",
            color : "#fc403f",
            rollPeriod : 5,
            strokeWidth:2,
            fillGraph: true,
            xlabel: 'Time',
            xLabelHeight : 14,
            legend : "always",
            labelsSeparateLines: "true",
            labelsDivStyles: {
                  'text-align': 'right',
                  'background': 'none'
                },}
        );
        var gh = new Dygraph(
            document.getElementById("graphHumid"), filenameH, {
            axisLabelFontSize : 10,
            axisLineColor : "rgb(20, 20, 20)",
            axisLabelColor : "rgb(20, 20, 20)",
            color : "#3eaaf2",
            rollPeriod : 5,
            strokeWidth:2,
            fillGraph: true,
            xlabel: 'Time',
            xLabelHeight : 14,
            legend : "always",
            labelsSeparateLines: "true",
            labelsDivStyles: {
                  'text-align': 'right',
                  'background': 'none'
                },}
        );
        var gp = new Dygraph(
            document.getElementById("graphPressure"), filenameP, {
            axisLabelFontSize : 10,
            axisLineColor : "rgb(20, 20, 20)",
            axisLabelColor : "rgb(20, 20, 20)",
            color : "#b5f23e",
            rollPeriod : 5,
            strokeWidth:2,
            fillGraph: true,
            xlabel: 'Time',
            xLabelHeight : 14,
            legend : "always",
            labelsSeparateLines: "true",
            labelsDivStyles: {
                  'text-align': 'right',
                  'background': 'none'
                },}
        );
  }
  </script>
</body>
