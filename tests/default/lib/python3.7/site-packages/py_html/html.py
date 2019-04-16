import os
import platform
import datetime
import inspect
import sys

pre_html_body = """<!DOCTYPE html>
<html>
   <head>
      <title>Automation Test Report</title>
      <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css"><style type="text/css">
         .panel-heading {
         padding: 0;
         }
         @media (min-width: 768px) {
         .pull-right-lg {
         float: left;
         }
         }
         @media (min-width: 992px) and (max-width: 1199px) {
         .pull-right-lg {
         float: right;
         }
         }
         @media (min-width: 768px) and (max-width: 991px) {
         .pull-right-lg {
         float: right;
         }
         }
         @media (min-width: 1200px) {
         .pull-right-lg {
         float: right;
         }
         }
         .left {
         float: left;
         }
         .metadata {
         overflow: auto;
         letter-spacing: 0.2px;
         border-color: white;
         line-height: 1.6;
         color: #4d4d4d;
         font-family: "Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;
         font-size: 13px;
         padding-bottom: 3px;
         }
         .panel-heading a {
         padding: 10px 15px;
         display: block;
         position: relative;
         text-decoration: none;
         }
         .panel-heading i.glyphicon-chevron-down {
         display: none;
         }
         .panel-heading i.glyphicon-chevron-right {
         display: inline-block;
         }
         .panel-heading.open i.glyphicon-chevron-down {
         display: inline-block;
         }
         .panel-heading.open i.glyphicon-chevron-right {
         display: none;
         }
         .generated-on {
         text-align: right;
         padding-bottom: 10px;
         }
         .panel-title b {
         padding-right: 10px;
         }
         .panel-heading .label-container {
         position: absolute;
         top: 8px;
         right: 8px;
         }
         .panel-heading .label-container label {
         margin-left: 5px;
         padding: 5px;
         }
         .navbar .label-container {
         position: absolute;
         right: 10px;
         top: 14px;
         }
         .navbar {
         margin-bottom: 10px;
         }
         .navbar .label {
         font-size: 20px;
         }
         .navbar .project-name {
         position: absolute;
         top: 10px;
         left: 50%;
         margin-left: -100px;
         text-align: center;
         font-size: 20px;
         font-weight: bold;
         }
         .tags {
         margin-left: 18px;
         margin-right: 20px;
         padding-top: 5px;
         margin-bottom: -4px;
         }
         .tag {
         font-size: 13px;
         color: #696969;
         letter-spacing: 0.3px;
         font-weight: bold;
         font-family: "Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;
         }
         .chart {

         padding-bottom: 40px;

         }
         div.chart div div svg rect {
         fill: #f5f5f5;
         height: 310px;

         }
         table.arguments {
         margin-left: 30px;
         margin-top: 1em;
         }
         #directory {
         background-color: #f0f0f0;
         }
         .screenshot {
         padding: 2% 0 2% 0;
         }
         .scenarioTitle {
         width: 80%
         }
         .description {
         background-color: white;
         border-color: white;
         line-height: 1.6;
         color: #6f6f6f;
         font-weight: 400;
         font-family: "Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;
         font-size: 14px;
         padding: 0.1em 0.5em 1.2em 1.5em
         }
         #scenario-description {
         padding-bottom: 1em;
         padding-left: 0.2em;
         }
         .scrollBar {
         overflow-x: scroll;
         }
         table {
         border-collapse: collapse;
         }
         table,
         th,
         td {
         border: 1px solid black;
         }
         th,
         td {
         text-align: left;
         padding: 8px;
         }
         th {
         background-color: #f5f5f5;
         color: black;
         }
         .info {
         background-color: #fbfbfb;
         }
         pre {
         display: block;
        	 padding: 10px;
         margin-top: 1em;
         margin-right: 3em;
         font-size: 13px;
         line-height: 1.42857143;
         word-break: break-all;
         word-wrap: break-word;
         color: #333;
         background-color: #f5f5f5;
         border: 1px solid #ccc;
         border-radius: 4px;
         }
         .step-duration {
         float: right;
         color: #BDBDBD;
         }
         .footer-div {
         text-align: right;
         vertical-align: middle;
         height: 3.5%;
         width: 100%;
         }
         .footer-container {
         margin-right: 10px;
         margin-top: 5px;
         width: 18%;
         z-index: 10;
         position: absolute;
         right: 0;
         bottom: 10px;
         text-align: center;
         background-color: transparent;
         }
         .footer-link {
         font-size: 13px;
         float: right;
         }
         .footer-link:hover {
         color: darkgray;
         }
         .steps {
         padding-left: 10px;
         padding-right: 10px;
         margin-bottom: -9px;
         }
         .all-features {
         padding-top: 0.6em;
         }
         .GuageChart {
         height: 600px;
         }
         div.GuageChart {
         	margin-left: 25px;
            margin-right: 0px;
            padding-top: -4px;
            margin-bottom: -4px;
         	height: 310px;
         	width: 100%;
            background-color: #f5f5f5;
         }


"""
pre_style_gauge_body = """</style> <meta charset="UTF-8"> </head> <body> <div class="navbar navbar-default navbar-static-top" role="navigation"> <div class="container"> <div class="navbar-header"> <a class="navbar-brand">Report</a> <div class="project-name visible-md visible-lg"><script src="https://drive.google.com/uc?export=view&id=1IcgsKMLJLVXJbcuHRSpyikmqwUOBxkRo"></script>
         <script src="https://www.amcharts.com/lib/3/gauge.js"></script>
         <script src="https://www.amcharts.com/lib/3/plugins/export/export.min.js"></script>
         <link rel="stylesheet" href="https://www.amcharts.com/lib/3/plugins/export/export.css" type="text/css" media="all" />
         <script src="https://www.amcharts.com/lib/3/themes/light.js"></script>
         <!-- Chart code -->
          <script>
                     var res = 0;
                     var GuageChart = AmCharts.makeChart("chartdiv", {
                         "theme": "light",
                         "type": "gauge",
                         "axes": [{
                             "topTextFontSize": 10,
                             "topTextYOffset": 70,
                             "axisColor": "#31d6ea",
                             "axisThickness": 1,
                             "endValue": 100,
                             "gridInside": true,
                             "inside": true,
                             "radius": "80%",
                             "valueInterval": 10,
                             "tickColor": "#67b7dc",
                             "startAngle": -90,
                             "endAngle": 90,
                             "bandOutlineAlpha": 0,

                         }],
                         "arrows": [{
                             "alpha": 0,
                             "innerRadius": "20%",
                             "nailRadius": 0,
                             "radius": "100%"
                         }]
                     });
                     setInterval(randomValue, 2000);

                     function randomValue(value) {
                         var value = res.toFixed(1);
                         GuageChart.arrows[0].setValue(value);
                         GuageChart.axes[0].setTopText(value + " % Passed");
                         // adjust darker band to new value
                         GuageChart.axes[0].bands[1].setEndValue(value);
                     }
                  </script>"""
passed_end = """</div> </div> </div> </div> </div> </div> </div> """
failed_end = """</p> </div> </div> </div> </div> </div> <div id="collapseScenariounhappy0_3" class="panel-collapse collapse"> <div class="panel-body"> <p class="scenario-container"> <div class="row steps"> <span class="label label-success" title="Success"><i class="glyphicon glyphicon-ok"></i></span> <span class="text"> <span class="keyword highlight">Given </span> <span> Fred runs a cucumber scenario</span> <span class="step-duration"> <1ms </span> </span> </p> </div> <p class="scenario-container"> <div class="row steps"> <span class="label label-success" title="Success"><i class="glyphicon glyphicon-ok"></i></span> <span class="text"> <span class="keyword highlight">When </span> <span> he left this step to be ambiguous</span> <span class="step-duration"> <1ms </span> </span> </p> </div> <p class="scenario-container"> <div class="row steps"> <span class="label label-success" title="Success"><i class="glyphicon glyphicon-ok"></i></span> <span class="text"> <span class="keyword highlight">Then </span> <span> cucumber-html-reporter should create HTML report with ambiguous steps</span> <span class="step-duration"> <1ms </span> </span> </p> </div> </div> </div> </div> </div> </div> </div> </div> </div> </div> </div> </div> </div> </div>"""
post_html_style_1 = """<!-- add something--> <div class="navbar-fixed-bottom row-fluid footer-div "> <div class="navbar-inner"> <div class="footer-container"> <a target="_blank" href="#"> <div class="text-muted footer-link"> Created by @Neova Solutions  </div> </a> </div> </div> </div> <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script> <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script> <script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.5.1/moment.min.js"></script> <script type="text/javascript" src="https://www.google.com/jsapi"></script> <script type="text/javascript"> google.load("visualization", "1", {packages: ["corechart"]}); google.setOnLoadCallback(function(){drawChart("""
post_html_style_2 = """) }); </script> <script> $(document).ready(function() { $('.collapse').on('hide.bs.collapse', function(e) { e.stopPropagation(); $(this).prev().removeClass('open'); }).on('show.bs.collapse', function(e) { e.stopPropagation(); $(this).prev().addClass('open'); }); $('a.toggle').on('click', function() { if ($(this).text() === 'Screenshot -') { $(this).text('Screenshot +'); $(this).next('a.screenshot').find('img').hide(); } else { $(this).text('Screenshot -'); $(this).next('a.screenshot').find('img').show(); } }); var $generated = $('.generated-on'); $generated.text('Generated ' + moment($generated.text()).fromNow()); }); function drawChart(chartData) { var data = google.visualization.arrayToDataTable([ ['Task', 'Cucumber Results'], ['Passed', chartData.passed], ['Failed', chartData.failed], ['Pending', chartData.pending], ['Undefined', chartData.notdefined], ['Ambiguous', chartData.ambiguous], ['Skipped', chartData.skipped] ]); var total = chartData.passed + chartData.failed + (chartData.pending || 0) + (chartData.notdefined || 0) + (chartData.ambiguous || 0) + (chartData.skipped || 0);var result=(chartData.passed/total)*100;
         res=result; var title; if (total === 1) { title = total + ' ' + chartData.title.slice(0, -1) } else { title = total + ' ' + chartData.title; } var options = { width: '650', height: 350, title: title, pieHole: 0.6, colors: ['#5cb85c', '#d9534f', '#999', '#5bc0de', '#428bca', '#f0ad4e'], fontSize: '11', fontName: '"Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif', slices: { 1: {offset: 0.0}, 2: {offset: 0.0}, 3: {offset: 0.0}, 4: {offset: 0.0}, 5: {offset: 0.0}, 6: {offset: 0.0} }, titleTextStyle: { fontSize: '13', color: '#5e5e5e' } }; var chart = new google.visualization.PieChart
(document.getElementById('piechart_' + chartData.title.toLowerCase())); chart.draw(data, options); } </script>"""
post_html_body = """</body>
</html>"""
test_res = {
            "passed": {
                "info": []
            },
            "failed": {
                "info": []
            },
            "skipped": {
               "info": []
            }
}


class TestStatus():

    total_passed = 0
    total_failed = 0
    total_skipped = 0
    total_test_case = 0

    def __init__(self,passed, failed, skipped, total_test):
        self.total_passed = passed
        self.total_failed = failed
        self.total_skipped = skipped
        self.total_test_case = total_test


class BuildTestData(object):
    failed_html = ""
    passed_html = ""
    total_passed = 0
    total_failed = 0
    total_skipped = 0
    total_test_case = 0
    env_setup = ""
    file_path = ""

    def __init__(self, passed, failed, skipped, total_test):
        self.total_passed = passed
        self.total_failed = failed
        self.total_skipped = skipped
        self.total_test_case = total_test

    def setup_environment_info(self, report_name, test_environment, browser, platform):
        try:
            passed_test = self.total_passed
            failed_test = self.total_failed
            date_and_time = str(datetime.datetime.now().strftime(" %I:%M %p %d-%b-%Y"))
            execution_start_time = str(datetime.datetime.now().strftime(" %I:%M %p %d-%b-%Y"))
            env_setup = """%s</div> <div class="label-container"> <span class="label label-success" title="scenarios Passed:" data-toggle="collapse" data-target="#collapseSuitehappy">Passed: %s </span> &nbsp;&nbsp;<span class="label label-danger" title="scenarios Failed: " data-toggle="collapse" data-target="#failed">Failed: %s </div> </div> </div> </div> <div class="container"> <div class="generated-on">%s</div> <div class="row"> <div class="chart col-lg-6 col-md-6"><div class="GuageChart" id="chartdiv"></div> </div> <div class="chart col-lg-6 col-md-6" id="piechart_scenarios"> </div> </div> <div class="panel panel-default"> <div class="panel-heading"> <h4 class="panel-title"> <a data-toggle="collapse" href="#metadataInfo"> <i class="glyphicon glyphicon-chevron-right"></i> <i class="glyphicon glyphicon-chevron-down"></i> <b> Environment </b> </a> </h4> </div> <div id="metadataInfo" class="panel-collapse collapse"> <div class="panel-body"> <div class="row"> <div class="clearfix metadata col-xs-12 col-sm-6 col-md-6 col-lg-6"> <div class=pull-left> <h5 style="font-weight:bold" > Data and Time: %s</h5> </div> </div> <div class="clearfix metadata col-xs-12 col-sm-6 col-md-6 col-lg-6"> <div class=pull-right-lg> <h5 style="font-weight:bold" > Test Environment: %s </h5> </div> </div> <div class="clearfix metadata col-xs-12 col-sm-6 col-md-6 col-lg-6"> <div class=pull-left> <h5 style="font-weight:bold" > Browser: %s</h5></div> </div> <div class="clearfix metadata col-xs-12 col-sm-6 col-md-6 col-lg-6"> <div class=pull-right-lg> <h5 style="font-weight:bold" > Platform: %s</h5></div> </div>  </div> </div> </div> </div>"""%(report_name,passed_test,failed_test,date_and_time,execution_start_time,test_environment,browser,platform)
            return env_setup
        except Exception, ex:
            print "Execption in generate_report method", ex

    def get_total_test_status(self,passed, failed, skipped, total_test):
        self.total_passed = passed
        self.total_failed = failed
        self.total_skipped = skipped
        self.total_test_case = total_test

    def get_failed_html_instance(self, method_name, description):
        failed_html=""" <div class="panel-heading">
                <h4 class="panel-title">
                  <a data-toggle="collapse" href="#collapseScenariohappy0_0">
                    <i class="glyphicon glyphicon-chevron-right"></i>
                    <i class="glyphicon glyphicon-chevron-down"></i>
                    <b>%s:</b>%s
                  </a>
                </h4>
              </div><br/>
        """%(method_name,description)
        return failed_html

    def get_passed_html_instance(self, method_name, description):
        passed_html=""" <div class="panel-heading">
                <h4 class="panel-title">
                  <a data-toggle="collapse" href="#collapseScenariohappy0_0">
                    <i class="glyphicon glyphicon-chevron-right"></i>
                    <i class="glyphicon glyphicon-chevron-down"></i>
                    <b>%s:</b>%s
                  </a>
                </h4>
              </div><br/>
        """%(method_name,description)
        return passed_html

    def generate_failed_data_for_html_report(self):
        for failed_test in test_res.get("failed")["info"]:
            description = failed_test.get('description')
            method_name = failed_test.get('test_name')
            self.failed_html+=self.get_failed_html_instance(method_name,description)
        return self.failed_html

    def generate_passed_data_for_html_report(self):
        for passed_test in test_res.get("passed")["info"]:
            description = passed_test.get('description')
            method_name = passed_test.get('test_name')
            self.passed_html+=self.get_passed_html_instance(method_name,description)
        return self.passed_html

    def add_pass_status_on_label(self):
        pre_style_passed = """<div class="all-features"> <div style="display: none;">No features</div> <div class="panel panel-default"> <div class="panel-heading" id="directory"> <h4 class="panel-title"> <a data-toggle="collapse" href="#collapseSuitehappy"> <i class="glyphicon glyphicon-chevron-right"></i> <i class="glyphicon glyphicon-chevron-down"></i> <b>PASSED</b> <span class="label-container"> <span class="label label-success" title="Passed">%s</span> </span> </a> </h4> </div> <div id="collapseSuitehappy" class="panel-collapse collapse"> <div class="panel-body"> <div class="row"><div class="panel-body">"""%(self.total_passed)
        return pre_style_passed

    def add_failed_status_on_lable(self):
        pre_style_failed = """<div class="panel panel-default"> <div class="panel-heading" id="directory"> <h4 class="panel-title"> <a data-toggle="collapse" href="#failed"> <i  class="glyphicon glyphicon-chevron-right"></i> <i class="glyphicon glyphicon-chevron-down"></i> <b>FAILED</b> <span   class="label-container"> <span  style="background-color:red" class="label label-success" title="Failed">%s</span> </span> </a> </h4> </div> <div id="failed" class="panel-collapse collapse"> <div class="panel-body"> <div class="row">  <div class="panel-body">"""%(self.total_failed)
        return pre_style_failed

    def create_test_report_folder(self):
        folder_name = os.path.abspath(self.file_path+"/test-output")
        try:
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
                return folder_name
            return folder_name
        except OSError as ex:
            print ex
            return None

    def generate_final_report(self):
        passed_body = self.generate_passed_data_for_html_report()
        failed_body = self.generate_failed_data_for_html_report()
        pre_style_passed = self.add_pass_status_on_label()
        pre_style_failed = self.add_failed_status_on_lable()
        pie_chart_result = """{ "title" : "Scenarios", "failed" : %s, "passed" : %s, "skipped" : %s }"""%(self.total_failed,self.total_passed,self.total_skipped)
        data = pre_html_body+pre_style_gauge_body+self.env_setup+pre_style_passed+"<div class='panel panel-default'>"+passed_body+passed_end+pre_style_failed+"<div class='panel panel-default'>"+failed_body+failed_end+post_html_style_1+pie_chart_result+post_html_style_2+post_html_body
        file_name = os.path.abspath(self.create_test_report_folder()+"/report.html")
        try:
            with open(file_name, "w") as html_file:
                html_file.writelines(data)
        except Exception, ex:
            print "Execption in generate_report method", ex


class AddLogger(object):
    passed = []
    failed = []
    skipped = []

    def mark_as_passed(self, method_name, description):
        pass_count = 1
        self.passed.append(pass_count)
        test_res.get("passed")["info"].append({"test_name":method_name,"description":description})

    def mark_as_failed(self, method_name, description):
        fail_count = 1
        self.failed.append(fail_count)
        test_res.get("failed")["info"].append({"test_name":method_name,"description":description})

    def mark_as_skipped(self, method_name, description):
        skip_count = 1
        self.skipped.append(skip_count)
        test_res.get("skipped")["info"].append({"test_name": method_name,"description": description})

    def get_total_passed_test(self):
        total_passed = sum(self.passed[0:len(self.passed)])
        return total_passed

    def get_total_failed_test(self):
        total_failed = sum(self.failed[0:len(self.failed)])
        return total_failed

    def get_total_skipped_test(self):
        total_skipped = sum(self.skipped[0:len(self.skipped)])
        return total_skipped


class Report(object):

    report_name = ""
    test_environment = ""
    browser_version = ""
    file_path = ""

    def start(self, report_name, test_environment, browser_version):
        self.report_name = report_name
        self.test_environment = test_environment
        self.browser_version = browser_version
        self.file_path = os.path.abspath(os.path.join(inspect.getsourcefile(sys._getframe(1)), os.pardir))

    def log_as_passed(self, method_name, description):
        AddLogger().mark_as_passed(method_name, description)

    def log_as_failed(self, method_name, description):
        AddLogger().mark_as_failed(method_name, description)

    def log_as_skipped(self, method_name, description):
        AddLogger().mark_as_skipped(method_name,description)

    def close(self):
        pass_test = AddLogger().get_total_passed_test()
        fail_test = AddLogger().get_total_failed_test()
        skip_test = AddLogger().get_total_skipped_test()
        total_test = pass_test+fail_test+skip_test
        operating_system = str(platform.system()+" "+platform.release())
        BuildTestData.file_path = self.file_path
        BuildTestData.env_setup = BuildTestData(pass_test, fail_test, skip_test, total_test).setup_environment_info(self.report_name,self.test_environment,self.browser_version,operating_system)
        BuildTestData(pass_test, fail_test, skip_test, total_test).generate_final_report()

