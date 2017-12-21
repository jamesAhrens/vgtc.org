var lis = d3.select("#breadcrumbs")
    .append("ul")
    .classed("breadcrumb", true)
    .selectAll("li")
    .data(breadCrumb)
    .enter()
    .append("li");
lis.append("a")
    .attr("href", function(d) { return d[1]; })
    .text(function(d) { return d[0]; });
lis.append("span").text(" ");
lis.append("span").classed("divider", true).text("/");
