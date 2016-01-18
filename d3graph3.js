function createGraph(){

  document.getElementById("graph").innerHTML = "";

  var d = new Date();
  var year = d.getFullYear();
  var month = ("0" + (d.getMonth() + 1)).slice(-2);
  var day = ("0" + (d.getDate())).slice(-2);
  //var filename = day + "_" + month + "_" + year + ".csv"

  var fileTxt = document.getElementById("files");
  var filename = fileTxt.options[fileTxt.selectedIndex].text;

  // Set the dimensions of the canvas / graph
  var marginTemp = {top: 30, right: 20, bottom: 30, left: 30},
      width = 600 - marginTemp.left - marginTemp.right,
      height = 300 - marginTemp.top - marginTemp.bottom;

  var marginHumid = {top: 30, right: 20, bottom: 30, left: 30},
      width = 600 - marginTemp.left - marginTemp.right,
      height = 300 - marginTemp.top - marginTemp.bottom;

  // Parse the date / time
  var parseDate = d3.time.format("%d/%m/%Y").parse;
  var parseTime = d3.time.format("%H:%M:%S").parse;

  // Set the ranges
  var x = d3.time.scale().range([0, width]);
  var y = d3.scale.linear().range([height, 0]);

  // Define the axes
  var xAxis = d3.svg.axis().scale(x)
      .orient("bottom").ticks(5).tickFormat(d3.time.format('%H:%M'));

  var yAxis = d3.svg.axis().scale(y)
      .orient("left").ticks(5);

  // Define the lines
  var tempLine = d3.svg.line()
      .x(function(d) { return x(d.time); })
      .y(function(d) { return y(d.temperature); });

  var humidLine = d3.svg.line()
      .x(function(d) { return x(d.time); })
      .y(function(d) { return y(d.humidity); });

  // Adds the svg canvas
  var svgTemp = d3.select("#graph")
      .append("svg")
          .attr("width", width + marginTemp.left + marginTemp.right)
          .attr("height", height + marginTemp.top + marginTemp.bottom)
      .append("g")
          .attr("transform",
                "translate(" + marginTemp.left + "," + marginTemp.top + ")");

  var svgHumid = d3.select("#graph")
      .append("svg")
          .attr("width", width + marginHumid.left + marginHumid.right)
          .attr("height", height + marginHumid.top + marginHumid.bottom)
      .append("g")
          .attr("transform",
                "translate(" + marginHumid.left + "," + marginHumid.top + ")");

  // Get the data
  d3.csv(filename, function(error, data) {
      data.forEach(function(d) {
          d.time = parseTime(d.time);
          d.temperature = +d.temperature-7;
          d.humidity = +d.humidity;
      });
      // Scale the range x time
      x.domain(d3.extent(data, function(d) { return d.time; }));
      // Scale the range of temperature
      y.domain([10, d3.max(data, function(d) { return d.temperature; })+2]);
      // Add the valueline path.
      svgTemp.append("path")
          .attr("class", "line")
          .attr("d", tempLine(data));
      // Add the X Axis
      svgTemp.append("g")
          .attr("class", "x axis")
          .attr("transform", "translate(0," + height + ")")
          .call(xAxis);
      // Add the Y Axis
      svgTemp.append("g")
          .attr("class", "y axis")
          .call(yAxis);

      // Scale the range of humidity
      y.domain([0, d3.max(data, function(d) { return d.humidity; })+2]);
      svgHumid.append("path")
          .attr("class", "line")
          .attr("d", humidLine(data))
          .style("stroke", "blue");
      // Add the X Axis
      svgHumid.append("g")
          .attr("class", "x axis")
          .attr("transform", "translate(0," + height + ")")
          .call(xAxis);
      // Add the Y Axis
      svgHumid.append("g")
          .attr("class", "y axis")
          .call(yAxis);
  });
}
