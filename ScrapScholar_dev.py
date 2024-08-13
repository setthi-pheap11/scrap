import csv
from bs4 import BeautifulSoup

html_content = """<div class="maincontent">


<!-- google_ad_section_start -->
<div id="catdesc"><h1 class="page-title" style="font-size: 23px; letter-spacing: .4px; margin-top: 10px;">List of Fellowship Scholarships, Grants, and Fellowships for International Students</h1></div>
<!-- google_ad_section_end -->
		

<div class="breadcrumbs">
    </div> 

		
<div style="margin: 0px 0px 10px 0px;"><script async="" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<ins class="adsbygoogle" style="display: block; height: 157px;" data-ad-format="fluid" data-ad-layout-key="-g7-1g-4j-e8+1k2" data-ad-client="ca-pub-4697326626447067" data-ad-slot="8513259196" data-adsbygoogle-status="done" data-ad-status="filled"><div id="aswift_2_host" style="border: none; height: 157px; width: 630px; margin: 0px; padding: 0px; position: relative; visibility: visible; background-color: transparent; display: inline-block;"><iframe id="aswift_2" name="aswift_2" browsingtopics="true" style="left:0;position:absolute;top:0;border:0;width:630px;height:157px;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" width="630" height="157" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allow="attribution-reporting; run-ad-auction" src="https://googleads.g.doubleclick.net/pagead/ads?client=ca-pub-4697326626447067&amp;output=html&amp;h=157&amp;slotname=8513259196&amp;adk=1851292588&amp;adf=58266513&amp;pi=t.ma~as.8513259196&amp;w=630&amp;abgtt=3&amp;lmt=1721288827&amp;rafmt=11&amp;format=630x157&amp;url=https%3A%2F%2Fwww.scholars4dev.com%2Fcategory%2Flevel-of-study%2Ffellowship%2F&amp;wgl=1&amp;uach=WyJXaW5kb3dzIiwiMTUuMC4wIiwieDg2IiwiIiwiMTI2LjAuNjQ3OC4xODIiLG51bGwsMCxudWxsLCI2NCIsW1siTm90L0EpQnJhbmQiLCI4LjAuMC4wIl0sWyJDaHJvbWl1bSIsIjEyNi4wLjY0NzguMTgyIl0sWyJHb29nbGUgQ2hyb21lIiwiMTI2LjAuNjQ3OC4xODIiXV0sMF0.&amp;dt=1721288827590&amp;bpp=1&amp;bdt=413&amp;idt=244&amp;shv=r20240716&amp;mjsv=m202407160101&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;cookie=ID%3D3baa9eef02cca264%3AT%3D1719998355%3ART%3D1721285918%3AS%3DALNI_MY6zCaGbCsiWx6RJz-RXRpypA0fOg&amp;gpic=UID%3D00000e70fa91a412%3AT%3D1719998355%3ART%3D1721285918%3AS%3DALNI_Ma7QD3lsc3i_IqiSZOvW6FBApAFhQ&amp;eo_id_str=ID%3D4abdd8e25f03b883%3AT%3D1719998355%3ART%3D1721285918%3AS%3DAA-Afjaz4TwlcBp33uTpZsFzocku&amp;prev_fmts=0x0%2C941x280&amp;nras=1&amp;correlator=4128941919393&amp;frm=20&amp;pv=1&amp;ga_vid=1032990896.1719998355&amp;ga_sid=1721288828&amp;ga_hid=1858978451&amp;ga_fc=1&amp;u_tz=420&amp;u_his=6&amp;u_h=1080&amp;u_w=1920&amp;u_ah=1032&amp;u_aw=1920&amp;u_cd=24&amp;u_sd=0.8&amp;dmc=8&amp;adx=10&amp;ady=539&amp;biw=961&amp;bih=1022&amp;scr_x=0&amp;scr_y=833&amp;eid=44759875%2C44759926%2C44759837%2C42532524%2C95334529%2C95334830%2C95337870%2C31085385%2C31084187%2C31078663%2C31078665%2C31078668%2C31078670&amp;oid=2&amp;pvsid=1353949908131480&amp;tmod=743055070&amp;uas=0&amp;nvt=3&amp;ref=https%3A%2F%2Fwww.scholars4dev.com%2Fsitemap%2F&amp;fc=1920&amp;brdim=286%2C64%2C286%2C64%2C1920%2C0%2C1555%2C913%2C982%2C1022&amp;vis=1&amp;rsz=%7C%7CeE%7C&amp;abl=CS&amp;pfx=0&amp;fu=1152&amp;bc=31&amp;bz=1.58&amp;td=1&amp;tdf=2&amp;psd=W251bGwsbnVsbCxudWxsLDNd&amp;nt=1&amp;ifi=3&amp;uci=a!3&amp;fsb=1&amp;dtd=248" data-google-container-id="a!3" tabindex="0" title="Advertisement" aria-label="Advertisement" data-google-query-id="CKKDusWMsIcDFUcrtwAduBcBoQ" data-load-complete="true"></iframe></div></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script></div>


			<div class="post clearfix" id="post-1908">

					
	

					<div class="entry clearfix">

						<h2><a href="https://www.scholars4dev.com/1908/phd-fellowships-for-international-students-in-hongkong/" rel="bookmark" title=" Link to Hong Kong PhD Fellowship Scheme for International Students">Hong Kong PhD Fellowship Scheme for International Students</a></h2>
												<p></p><div style="width:46%; float: left; padding-right: 8%; display: inline;" class="post_column_1"><p><em>Hong Kong RGC<br>
</em>Doctoral (PhD) Degree </p></div> <div style="width:46%; float: left; padding-right: 0; display: inline;" class="post_column_1"><p> <strong>Deadline:</strong> 1 Dec 2023 (annual)<br>
Study in:&nbsp; Hong Kong, China<br>
Course starts&nbsp; September 2024 </p></div><p></p>
											</div>

					<div class="postdate clearfix">
	<div class="left">

Last updated: 15 Nov 2023 | <span style="color: #ff0000;">CURRENTLY CLOSED</span>


	</div>

	<div class="right">
		<a class="more-link" href="https://www.scholars4dev.com/1908/phd-fellowships-for-international-students-in-hongkong/" rel="bookmark" title="More about Hong Kong PhD Fellowship Scheme for International Students">Read More</a>
	</div>
</div>


				</div>




			<div class="post clearfix" id="post-4900">

					
	

					<div class="entry clearfix">

						<h2><a href="https://www.scholars4dev.com/4900/commonwealth-scholarships-for-developing-commonwealth-countries/" rel="bookmark" title=" Link to Commonwealth Master’s Scholarships for Developing Commonwealth Countries">Commonwealth Master’s Scholarships for Developing Commonwealth Countries</a></h2>
												<p></p><div style="width:46%; float: left; padding-right: 8%; display: inline;" class="post_column_1"><p><em>DFID</em><br>
Masters Degree</p></div> <div style="width:46%; float: left; padding-right: 0; display: inline;" class="post_column_1"><p> <strong>Deadline:</strong> 17 Oct 2023 (annual)<br>
Study in: UK<br>
Course starts Sept/Oct 2024 </p></div><p></p>
											</div>

					<div class="postdate clearfix">
	<div class="left">

Last updated: 12 Sep 2023 | <span style="color: #ff0000;">CURRENTLY CLOSED</span>


	</div>

	<div class="right">
		<a class="more-link" href="https://www.scholars4dev.com/4900/commonwealth-scholarships-for-developing-commonwealth-countries/" rel="bookmark" title="More about Commonwealth Master’s Scholarships for Developing Commonwealth Countries">Read More</a>
	</div>
</div>


				</div>




			<div class="post clearfix" id="post-1877">

					
	

					<div class="entry clearfix">

						<h2><a href="https://www.scholars4dev.com/1877/aauw-international-fellowships-in-usa-for-women/" rel="bookmark" title=" Link to AAUW International Fellowships in USA for Women">AAUW International Fellowships in USA for Women</a></h2>
												<p></p><div style="width:46%; float: left; padding-right: 8%; display: inline;" class="post_column_1"><p><em>AAUW<br>
</em>Masters/PhD/Postdoctoral </p></div> <div style="width:46%; float: left; padding-right: 0; display: inline;" class="post_column_1"><p> <strong>Deadline:</strong> 15 Nov 2023 (annual)<br>
Study in: USA<br>
Next course starts 1 July 2024 </p></div><p></p>
											</div>

					<div class="postdate clearfix">
	<div class="left">

Last updated: 15 Aug 2023 | <span style="color: #ff0000;">CURRENTLY CLOSED</span>


	</div>

	<div class="right">
		<a class="more-link" href="https://www.scholars4dev.com/1877/aauw-international-fellowships-in-usa-for-women/" rel="bookmark" title="More about AAUW International Fellowships in USA for Women">Read More</a>
	</div>
</div>


				</div>




			<div class="post clearfix" id="post-2887">

					
	

					<div class="entry clearfix">

						<h2><a href="https://www.scholars4dev.com/2887/hubert-humphrey-fellowships-for-international-students/" rel="bookmark" title=" Link to Hubert Humphrey Fellowships in USA for International Students">Hubert Humphrey Fellowships in USA for International Students</a></h2>
												<p></p><div style="width:46%; float: left; padding-right: 8%; display: inline;" class="post_column_1"><p><em>USA Government<br>
</em>Non-degree </p></div> <div style="width:46%; float: left; padding-right: 0; display: inline;" class="post_column_1"><p> <strong>Deadline: </strong>before 1 Oct&nbsp;(annual)<br>
Study in:&nbsp; USA<br>
Program starts Apr-Sept 2024 </p></div><p></p>
											</div>

					<div class="postdate clearfix">
	<div class="left">

Last updated: 23 May 2023 | <span style="color: #ff0000;"></span>


	</div>

	<div class="right">
		<a class="more-link" href="https://www.scholars4dev.com/2887/hubert-humphrey-fellowships-for-international-students/" rel="bookmark" title="More about Hubert Humphrey Fellowships in USA for International Students">Read More</a>
	</div>
</div>


				</div>




			<div class="post clearfix" id="post-2750">

					
	

					<div class="entry clearfix">

						<h2><a href="https://www.scholars4dev.com/2750/robert-s-mcnamara-phd-research-fellowships/" rel="bookmark" title=" Link to Robert S. McNamara Phd Research Fellowships">Robert S. McNamara Phd Research Fellowships</a></h2>
												<p></p><div style="width:46%; float: left; padding-right: 8%; display: inline;" class="post_column_1"><p><em>World Bank</em><br>
PhD Fellowships </p></div> <div style="width:46%; float: left; padding-right: 0; display: inline;" class="post_column_1"><p> <strong>Deadline:</strong> 3 April 2023 (annual)<br>
Study in:&nbsp; USA<br>
Research starts Sept 2023-May 2024 </p></div><p></p>
											</div>

					<div class="postdate clearfix">
	<div class="left">

Last updated: 28 Feb 2023 | <span style="color: #ff0000;"></span>


	</div>

	<div class="right">
		<a class="more-link" href="https://www.scholars4dev.com/2750/robert-s-mcnamara-phd-research-fellowships/" rel="bookmark" title="More about Robert S. McNamara Phd Research Fellowships">Read More</a>
	</div>
</div>


				</div>




			<div class="post clearfix" id="post-27316">

					
	

					<div class="entry clearfix">

						<h2><a href="https://www.scholars4dev.com/27316/2023-ibrahim-leadership-fellowships/" rel="bookmark" title=" Link to 2023 Ibrahim Leadership Fellowships">2023 Ibrahim Leadership Fellowships</a></h2>
												<p></p><div style="width:46%; float: left; padding-right: 8%; display: inline;" class="post_column_1"><p><em>Mo Ibrahim Foundation<br>
</em>Leadership Fellowships </p></div> <div style="width:46%; float: left; padding-right: 0; display: inline;" class="post_column_1"><p> <strong>Deadline:</strong> 21 Oct 2022 (annual)<br>
Country: Côte&nbsp;d’Ivoire/Ethiopia/Switzerland<br>
Fellowship starts 2023 </p></div><p></p>
											</div>

					<div class="postdate clearfix">
	<div class="left">

Last updated: 16 Aug 2022 | <span style="color: #ff0000;">CURRENTLY CLOSED</span>


	</div>

	<div class="right">
		<a class="more-link" href="https://www.scholars4dev.com/27316/2023-ibrahim-leadership-fellowships/" rel="bookmark" title="More about 2023 Ibrahim Leadership Fellowships">Read More</a>
	</div>
</div>


				</div>




			<div class="post clearfix" id="post-26981">

					
	

					<div class="entry clearfix">

						<h2><a href="https://www.scholars4dev.com/26981/epflglobaleaders-fellowship-programme/" rel="bookmark" title=" Link to EPFLglobaLeaders Fellowship Programme">EPFLglobaLeaders Fellowship Programme</a></h2>
												<p></p><div style="width:46%; float: left; padding-right: 8%; display: inline;" class="post_column_1"><p><em>EPFL</em><em><br>
</em>PhD Degree/Fellowships </p></div> <div style="width:46%; float: left; padding-right: 0; display: inline;" class="post_column_1"><p> <strong>Deadline:</strong> 15 April 2021<br>
Study in:&nbsp; Switzerland<br>
Fellowship starts 1 Nov 2021-1 March 2022. </p></div><p></p>
											</div>

					<div class="postdate clearfix">
	<div class="left">

Last updated: 16 Feb 2021 | <span style="color: #ff0000;">CURRENTLY CLOSED</span>


	</div>

	<div class="right">
		<a class="more-link" href="https://www.scholars4dev.com/26981/epflglobaleaders-fellowship-programme/" rel="bookmark" title="More about EPFLglobaLeaders Fellowship Programme">Read More</a>
	</div>
</div>


				</div>




			<div class="post clearfix" id="post-24795">

					
	

					<div class="entry clearfix">

						<h2><a href="https://www.scholars4dev.com/24795/russell-e-train-fellowships/" rel="bookmark" title=" Link to Russell E. Train Fellowships">Russell E. Train Fellowships</a></h2>
												<p></p><div style="width:46%; float: left; padding-right: 8%; display: inline;" class="post_column_1"><p><em>World Wildlife Fund, Russell E. Train Education for Nature Program<br>
</em>Masters, PhD Degree </p></div> <div style="width:46%; float: left; padding-right: 0; display: inline;" class="post_column_1"><p> <strong>Deadline:</strong> 1 March 2020 (Annual)<br>
Study in: Malaysia<br>
Course starts University-dependent </p></div><p></p>
											</div>

					<div class="postdate clearfix">
	<div class="left">

Last updated: 10 Feb 2020 | <span style="color: #ff0000;"></span>


	</div>

	<div class="right">
		<a class="more-link" href="https://www.scholars4dev.com/24795/russell-e-train-fellowships/" rel="bookmark" title="More about Russell E. Train Fellowships">Read More</a>
	</div>
</div>


				</div>




			<div class="post clearfix" id="post-19483">

					
	

					<div class="entry clearfix">

						<h2><a href="https://www.scholars4dev.com/19483/2017-future-global-leaders-fellowship/" rel="bookmark" title=" Link to 2020 Fortis Fellowship">2020 Fortis Fellowship</a></h2>
												<p></p><div style="width:46%; float: left; padding-right: 8%; display: inline;" class="post_column_1"><p><em>Future Leaders Foundation<br>
</em>Training/Fellowship&nbsp;</p></div> <div style="width:46%; float: left; padding-right: 0; display: inline;" class="post_column_1"><p> <strong>Deadline:</strong> 26 March 2020 (annual)<br>
Study in:&nbsp; USA<br>
Fellowship starts August 2020 </p></div><p></p>
											</div>

					<div class="postdate clearfix">
	<div class="left">

Last updated: 01 Jan 2020 | <span style="color: #ff0000;">CURRENTLY CLOSED</span>


	</div>

	<div class="right">
		<a class="more-link" href="https://www.scholars4dev.com/19483/2017-future-global-leaders-fellowship/" rel="bookmark" title="More about 2020 Fortis Fellowship">Read More</a>
	</div>
</div>


				</div>




			<div class="post clearfix" id="post-20623">

					
	

					<div class="entry clearfix">

						<h2><a href="https://www.scholars4dev.com/20623/ofid-development-leader-scholarship-to-attend-the-one-young-world-summit-2017/" rel="bookmark" title=" Link to OFID Development Leaders Scholarship to attend the One Young World Summit 2018">OFID Development Leaders Scholarship to attend the One Young World Summit 2018</a></h2>
												<p></p><div style="width:46%; float: left; padding-right: 8%; display: inline;" class="post_column_1"><p><em>OFID<br>
</em>Conference </p></div> <div style="width:46%; float: left; padding-right: 0; display: inline;" class="post_column_1"><p> <strong>Deadline:</strong>&nbsp;20 July 2018<br>
Venue: &nbsp;The Hague, Netherlands<br>
Conference dates: 17-20 October 2018</p></div><p></p>
											</div>

					<div class="postdate clearfix">
	<div class="left">

Last updated: 09 Jul 2018 | <span style="color: #ff0000;">CURRENTLY CLOSED</span>


	</div>

	<div class="right">
		<a class="more-link" href="https://www.scholars4dev.com/20623/ofid-development-leader-scholarship-to-attend-the-one-young-world-summit-2017/" rel="bookmark" title="More about OFID Development Leaders Scholarship to attend the One Young World Summit 2018">Read More</a>
	</div>
</div>


				</div>




			<div class="post clearfix" id="post-1447">

					
	

					<div class="entry clearfix">

						<h2><a href="https://www.scholars4dev.com/1447/international-organizations-mba-programme-for-developing-countries/" rel="bookmark" title=" Link to IO-MBA Program Scholarships at University of Geneva">IO-MBA Program Scholarships at University of Geneva</a></h2>
												<p></p><div style="width:46%; float: left; padding-right: 8%; display: inline;" class="post_column_1"><p><em>University of Geneva<br>
</em>Masters (MS) Degree </p></div> <div style="width:46%; float: left; padding-right: 0; display: inline;" class="post_column_1"><p> <strong>Deadline:</strong>&nbsp;30 June 2019<br>
Study in:&nbsp; Geneva, Switzerland<br>
Course starts September 2019 </p></div><p></p>
											</div>

					<div class="postdate clearfix">
	<div class="left">

Last updated: 03 Oct 2016 | <span style="color: #ff0000;">CURRENTLY CLOSED</span>


	</div>

	<div class="right">
		<a class="more-link" href="https://www.scholars4dev.com/1447/international-organizations-mba-programme-for-developing-countries/" rel="bookmark" title="More about IO-MBA Program Scholarships at University of Geneva">Read More</a>
	</div>
</div>


				</div>



			
			<div style="margin: 0px 0px 10px 0px;"><script async="" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<ins class="adsbygoogle" style="display: block; height: 118px;" data-ad-format="fluid" data-ad-layout-key="-g7-1g-4j-e8+1k2" data-ad-client="ca-pub-4697326626447067" data-ad-slot="8513259196" data-adsbygoogle-status="done" data-ad-status="filled"><div id="aswift_3_host" style="border: none; height: 118px; width: 630px; margin: 0px; padding: 0px; position: relative; visibility: visible; background-color: transparent; display: inline-block; overflow: hidden;"><iframe id="aswift_3" name="aswift_3" browsingtopics="true" style="left: 0px; position: absolute; top: 0px; border: 0px; width: 630px; height: 118px;" sandbox="allow-forms allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-top-navigation-by-user-activation" width="630" height="118" frameborder="0" marginwidth="0" marginheight="0" vspace="0" hspace="0" allowtransparency="true" scrolling="no" allow="attribution-reporting; run-ad-auction" src="https://googleads.g.doubleclick.net/pagead/ads?client=ca-pub-4697326626447067&amp;output=html&amp;h=157&amp;slotname=8513259196&amp;adk=1851292588&amp;adf=131783438&amp;pi=t.ma~as.8513259196&amp;w=630&amp;abgtt=3&amp;lmt=1721288827&amp;rafmt=11&amp;format=630x157&amp;url=https%3A%2F%2Fwww.scholars4dev.com%2Fcategory%2Flevel-of-study%2Ffellowship%2F&amp;wgl=1&amp;uach=WyJXaW5kb3dzIiwiMTUuMC4wIiwieDg2IiwiIiwiMTI2LjAuNjQ3OC4xODIiLG51bGwsMCxudWxsLCI2NCIsW1siTm90L0EpQnJhbmQiLCI4LjAuMC4wIl0sWyJDaHJvbWl1bSIsIjEyNi4wLjY0NzguMTgyIl0sWyJHb29nbGUgQ2hyb21lIiwiMTI2LjAuNjQ3OC4xODIiXV0sMF0.&amp;dt=1721288827591&amp;bpp=1&amp;bdt=415&amp;idt=253&amp;shv=r20240716&amp;mjsv=m202407160101&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;cookie=ID%3D3baa9eef02cca264%3AT%3D1719998355%3ART%3D1721285918%3AS%3DALNI_MY6zCaGbCsiWx6RJz-RXRpypA0fOg&amp;gpic=UID%3D00000e70fa91a412%3AT%3D1719998355%3ART%3D1721285918%3AS%3DALNI_Ma7QD3lsc3i_IqiSZOvW6FBApAFhQ&amp;eo_id_str=ID%3D4abdd8e25f03b883%3AT%3D1719998355%3ART%3D1721285918%3AS%3DAA-Afjaz4TwlcBp33uTpZsFzocku&amp;prev_fmts=0x0%2C941x280%2C630x157&amp;nras=1&amp;correlator=4128941919393&amp;frm=20&amp;pv=1&amp;ga_vid=1032990896.1719998355&amp;ga_sid=1721288828&amp;ga_hid=1858978451&amp;ga_fc=1&amp;u_tz=420&amp;u_his=6&amp;u_h=1080&amp;u_w=1920&amp;u_ah=1032&amp;u_aw=1920&amp;u_cd=24&amp;u_sd=0.8&amp;dmc=8&amp;adx=10&amp;ady=2346&amp;biw=961&amp;bih=1022&amp;scr_x=0&amp;scr_y=833&amp;eid=44759875%2C44759926%2C44759837%2C42532524%2C95334529%2C95334830%2C95337870%2C31085385%2C31084187%2C31078663%2C31078665%2C31078668%2C31078670&amp;oid=2&amp;pvsid=1353949908131480&amp;tmod=743055070&amp;uas=0&amp;nvt=3&amp;ref=https%3A%2F%2Fwww.scholars4dev.com%2Fsitemap%2F&amp;fc=1920&amp;brdim=286%2C64%2C286%2C64%2C1920%2C0%2C1555%2C913%2C982%2C1022&amp;vis=1&amp;rsz=%7C%7CeEbr%7C&amp;abl=CS&amp;pfx=0&amp;fu=1152&amp;bc=31&amp;bz=1.58&amp;td=1&amp;tdf=2&amp;psd=W251bGwsbnVsbCxudWxsLDNd&amp;nt=1&amp;ifi=4&amp;uci=a!4&amp;btvi=1&amp;fsb=1&amp;dtd=258" data-google-container-id="a!4" tabindex="0" title="Advertisement" aria-label="Advertisement" data-google-query-id="CJLBusWMsIcDFZvncwEdxywNRw" data-load-complete="true"></iframe></div></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script></div>


				<center><div class="wp-pagenavi" role="navigation">
<span class="pages">Page 1 of 2</span><span aria-current="page" class="current">1</span><a class="page larger" title="Page 2" href="https://www.scholars4dev.com/category/level-of-study/fellowship/page/2/">2</a><a class="nextpostslink" rel="next" aria-label="Next Page" href="https://www.scholars4dev.com/category/level-of-study/fellowship/page/2/">»</a>
</div></center> 

<p>			</p><div id="topsearch3" class="clearfix">
				<form id="searchform" method="get" action="https://www.scholars4dev.com/"><input type="text" value="" onfocus="if (this.value == '') {this.value = '';}" onblur="if (this.value == '') {this.value = '';}" size="18" maxlength="50" name="s" id="searchfield"><input type="image" src="https://www.scholars4dev.com/wp-content/themes/wp-jazz/images/blank.gif" id="submitbutton" alt="go"></form>
			</div>

<p></p>

				</div>"""

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract the relevant data
scholarships = []

# Loop through each scholarship post
for post in soup.find_all('div', class_='post clearfix'):
    title_tag = post.find('h2').find('a')
    title = title_tag.text.strip()
    link = title_tag['href']
    
    columns = post.find_all('div', class_='post_column_1')
    details_1 = columns[0].text.strip() if len(columns) > 0 else ""
    details_2 = columns[1].text.strip() if len(columns) > 1 else ""
    
    last_updated_tag = post.find('div', class_='postdate clearfix').find('div', class_='left')
    last_updated = last_updated_tag.text.strip() if last_updated_tag else ""
    
    more_link_tag = post.find('a', class_='more-link')
    more_link = more_link_tag['href'] if more_link_tag else ""
    
    scholarships.append([title, link, details_1, details_2, last_updated, more_link])

# Save the data to a CSV file
csv_file = 'scholarships.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Link', 'Details 1', 'Details 2', 'Last Updated', 'More Link'])
    writer.writerows(scholarships)

print(f"Data has been scraped and saved to {csv_file}")
    