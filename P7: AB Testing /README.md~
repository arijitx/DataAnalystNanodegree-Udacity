# <span class="c26 c9 c38">P7 A/B TESTING</span>

<span class="c1"></span>

<span class="c1"></span>

## <span class="c2 c25">Experiment Overview: Free Trial Screener</span>

<span class="c1"></span>

<span class="c1">At the time of this experiment, Udacity courses currently have two options on the home page: "start free trial", and "access course materials". If the student clicks "start free trial", they will be asked to enter their credit card information, and then they will be enrolled in a free trial for the paid version of the course. After 14 days, they will automatically be charged unless they cancel first. If the student clicks "access course materials", they will be able to view the videos and take the quizzes for free, but they will not receive coaching support or a verified certificate, and they will not submit their final project for feedback.</span>

<span class="c1"></span>

<span class="c2">In the experiment, Udacity tested a change where if the student clicked "start free trial", they were asked how much time they had available to devote to the course. If the student indicated 5 or more hours per week, they would be taken through the checkout process as usual. If they indicated fewer than 5 hours per week, a message would appear indicating that Udacity courses usually require a greater time commitment for successful completion, and suggesting that the student might like to access the course materials for free. At this point, the student would have the option to continue enrolling in the free trial, or access the course materials for free instead.</span><span class="c2 c45">[This screenshot](https://www.google.com/url?q=https://drive.google.com/a/knowlabs.com/file/d/0ByAfiG8HpNUMakVrS0s4cGN2TjQ/view?usp%3Dsharing&sa=D&ust=1469975802506000&usg=AFQjCNEsPzrWbj_1EKaxoMgeA1wxYzIiSw)</span><span class="c1"> shows what the experiment looks like.</span>

<span class="c1"></span>

<span class="c2">The hypothesis was that this might set clearer expectations for students upfront, thus reducing the number of frustrated students who left the free trial because they didn't have enough time</span><span class="c17 c2 c31">—</span><span class="c1">without significantly reducing the number of students to continue past the free trial and eventually complete the course. If this hypothesis held true, Udacity could improve the overall student experience and improve coaches' capacity to support students who are likely to complete the course.</span>

<span class="c1"></span>

<span class="c1">The unit of diversion is a cookie, although if the student enrolls in the free trial, they are tracked by user-id from that point forward. The same user-id cannot enroll in the free trial twice. For users that do not enroll, their user-id is not tracked in the experiment, even if they were signed in when they visited the course overview page.</span>

<span class="c1"></span>

# <span class="c22 c2"></span>

<span class="c1"></span>

# <span class="c2 c22">Experiment Design</span>

## <span class="c8">Metric Choice</span>

<span class="c1"></span>

<span class="c13 c2">List which metrics you will use as invariant metrics and evaluation metrics here. (These should be the same metrics you chose in the "Choosing Invariant Metrics" and "Choosing Evaluation Metrics" quizzes.)</span>

<span class="c13 c2"></span>

<span class="c1">Invariant Metrics :</span>

<span class="c2">-</span> <span class="c18 c17 c2">Number of cookies</span>

<span class="c18 c17 c2">- Number of clicks</span>

<span class="c18 c17 c2"></span>

<span class="c34 c26 c17 c2">Evaluation Metrics :</span>

<span class="c26 c17 c2">-</span> <span class="c18 c17 c2">Gross conversion</span>

<span class="c18 c17 c2">- Retention</span>

<span class="c26 c17 c2 c19">- Net conversio</span><span class="c26 c17 c2 c19">n</span>

<span class="c1"></span>

<span class="c13 c2">For each metric, explain both why you did or did not use it as an invariant metric and why you did or did not use it as an evaluation metric. Also, state what results you will look for in your evaluation metrics in order to launch the experiment.</span>

<span class="c13 c2"></span>

<span class="c42 c2">INVARIANT METRICS</span>

<span class="c9">Number of cookies:</span><span class="c2"> </span>

<span class="c1">That is, number of unique cookies to view the course overview page. This is page comes before the experiment starts and independent from the experiment . This is evenly distributed among the experiment and control group .</span>

*   <span class="c1"></span>

<span class="c0">Number of clicks:</span>

<span class="c2">That is the number of unique cookies to click the "Start free tria</span><span class="c2">l"</span> <span class="c2">button which</span><span class="c2"> </span><span class="c1">happens before the free trial screener is trigger so it is independent from the experiment and It is evenly distributed among the Control and Experiment groups.</span>

<span class="c1"></span>

<span class="c2 c42">EVALUATION METRICS</span>

<span class="c0">Gross conversion:</span>

<span class="c1">That is, number of user-ids to complete checkout and enroll in the free trial divided by number of unique cookies to click the "Start free trial" . This is the direct result of the experiment thus suitable to be an evaluation metric .So for our experiment we will test whether adding the time commitment option will make any change in the gross conversion of the experiment group from the control group and whether the change is significant .</span>

<span class="c1"></span>

<span class="c0"></span>

<span class="c0"></span>

<span class="c0">Retention:</span>

<span class="c1">That is, number of user-ids to remain enrolled past the 14-day boundary and thus make at least one payment divided by number of user-ids to complete checkout. This is also suitable to be an evaluation metric . Retention is highly dependent on the experiment . High retention will mean higher number of enrolled students who have paid at least once . So for our experiment we will test whether adding the time commitment option will make any change in the Retention of the experiment group from the control group and whether the change is significant .</span>

<span class="c1"></span>

<span class="c1"></span>

<span class="c0">Net conversion:</span>

<span class="c1">That is, number of user-ids to remain enrolled past the 14-day boundary (and thus make at least one payment) divided by the number of unique cookies to click the "Start free trial" button. Net Conversion will show the number of students who will be paid students after the 14 day free trial . So for our experiment we will test whether adding the time commitment option will make any change in the net conversion of the experiment group from the control group and whether the change is significant .</span>

<span class="c2 c13"></span>

<span class="c42 c2">NOT TAKEN AS EVALUATION OR INVARIANT METRICS</span>

<span class="c9">Click-through-probability:</span><span class="c1"> </span>

<span class="c1">That is, number of unique cookies to click the "Start free trial" button divided by number of unique cookies to view the course overview page.This won't be dependent on the experiment and it is also not guaranteed that the click through probability will be distributed evenly among the control and experiment group .</span>

<span class="c1"></span>

<span class="c0">Number of user-ids:</span>

<span class="c1">That is, number of users who enroll in the free trial . This is not an ideal metric for both evaluation and invariant . This will be dependent on the experiment but can vary drastically between the control and experiment group .</span>

<span class="c1"></span>

## <span class="c8">Measuring Standard Deviation</span>

<span class="c13 c2">List the standard deviation of each of your evaluation metrics. (These should be the answers from the "Calculating standard deviation" quiz.)</span>

<span class="c1"></span>

<a id="t.1224fb31f2fd59d61dcc6485f27fb5dca33980e6"></a><a id="t.0"></a>

<table class="c32">

<tbody>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c0">METRICS NAME</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0">STANDARD DEVIATION</span>

</td>

</tr>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c1">Gross Conversion</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c1">0.0202</span>

</td>

</tr>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c1">Retention</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c1">0.0549</span>

</td>

</tr>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c1">Net Conversion</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c1">0.0156</span>

</td>

</tr>

</tbody>

</table>

<span class="c13 c2">For each of your evaluation metrics, indicate whether you think the analytic estimate would be comparable to the the empirical variability, or whether you expect them to be different (in which case it might be worth doing an empirical estimate if there is time). Briefly give your reasoning in each case.</span>

<span class="c13 c2"></span>

<span class="c2 c19">Both Gross and Net Conversion are measured per number of cookies clicked in the ‘Start Free Trial’ button, here number of cookies is also the unit of diversion .</span> <span class="c18 c17 c2">Here, the unit of diversion is equal to unit of analysis . So the analytical estimate would be comparable to the empirical variability.</span>

<span class="c18 c17 c2"></span>

<span class="c26 c17 c2 c19">Here Retention is measured per the</span> <span class="c17 c2 c19">number of user-ids .</span> <span class="c26 c17 c2 c19">Here, the unit of diversion is not equal to unit of analysis</span><span class="c29 c2"> .</span> <span class="c18 c17 c2">So the analytical estimate and the empirical variability will be different.</span>

<span class="c13 c2"></span>

<span class="c1"></span>

## <span class="c8">Sizing</span>

### <span class="c23 c9">Number of Samples vs. Power</span>

<span class="c13 c2">Indicate whether you will use the Bonferroni correction during your analysis phase, and give the number of pageviews you will need to power you experiment appropriately. (These should be the answers from the "Calculating Number of Pageviews" quiz.)</span>

<span class="c24 c2"></span>

<span class="c2">No I will not use the Bonferroni correction during the analysis phase because</span> <span class="c17 c2 c19 c26">t</span><span class="c17 c2 c18">he metrics in the experiment has high correlation .</span>

<span class="c18 c17 c2"></span>

<a id="t.213d15c9b512f0c3804a1261f068bf3bada8a957"></a><a id="t.1"></a>

<table class="c32">

<tbody>

<tr class="c14">

<td class="c28" colspan="1" rowspan="1">

<span class="c18 c9 c17">Metric Name</span>

</td>

<td class="c35" colspan="1" rowspan="1">

<span class="c18 c9 c17">Dmin</span>

</td>

<td class="c20" colspan="1" rowspan="1">

<span class="c18 c9 c17">Baseline Conversion</span>

</td>

<td class="c12" colspan="1" rowspan="1">

<span class="c18 c9 c17">Samples Needed</span>

</td>

<td class="c11" colspan="1" rowspan="1">

<span class="c18 c9 c17">Total PageViews</span>

</td>

</tr>

<tr class="c14">

<td class="c28" colspan="1" rowspan="1">

<span class="c18 c17 c2">Gross Conversion</span>

</td>

<td class="c35" colspan="1" rowspan="1">

<span class="c18 c17 c2">0.01</span>

</td>

<td class="c20" colspan="1" rowspan="1">

<span class="c17 c2 c19">20.625 %</span>

</td>

<td class="c12" colspan="1" rowspan="1">

<span class="c18 c17 c2">25835</span>

</td>

<td class="c11" colspan="1" rowspan="1">

<span class="c18 c17 c2">645875</span>

</td>

</tr>

<tr class="c14">

<td class="c28" colspan="1" rowspan="1">

<span class="c18 c17 c2">Retention</span>

</td>

<td class="c35" colspan="1" rowspan="1">

<span class="c18 c17 c2">0.01</span>

</td>

<td class="c20" colspan="1" rowspan="1">

<span class="c18 c17 c2">53 %</span>

</td>

<td class="c12" colspan="1" rowspan="1">

<span class="c18 c17 c2">39115</span>

</td>

<td class="c11" colspan="1" rowspan="1">

<span class="c18 c17 c2">4741212</span>

</td>

</tr>

<tr class="c14">

<td class="c28" colspan="1" rowspan="1">

<span class="c18 c17 c2">Net Conversion</span>

</td>

<td class="c35" colspan="1" rowspan="1">

<span class="c18 c17 c2">0.0075</span>

</td>

<td class="c20" colspan="1" rowspan="1">

<span class="c17 c2 c19">10.93125 %</span>

</td>

<td class="c12" colspan="1" rowspan="1">

<span class="c18 c17 c2">27413</span>

</td>

<td class="c11" colspan="1" rowspan="1">

<span class="c18 c17 c2">685325</span>

</td>

</tr>

</tbody>

</table>

<span class="c18 c17 c2"></span>

### <span class="c23 c9"></span>

### <span class="c23 c9">Duration vs. Exposure</span>

<span class="c13 c2">Indicate what fraction of traffic you would divert to this experiment and, given this, how many days you would need to run the experiment. (These should be the answers from the "Choosing Duration and Exposure" quiz.)</span>

<span class="c13 c2"></span>

<span class="c13 c2"></span>

<a id="t.947f4c506607636d6d2a939cc77c60a4ee0f3e96"></a><a id="t.2"></a>

<table class="c32">

<tbody>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c0">Percentage of Traffic</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c1">50%</span>

</td>

</tr>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c0">Days Required</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c1">35</span>

</td>

</tr>

</tbody>

</table>

<span class="c13 c2"></span>

<span class="c1"></span>

<span class="c13 c2">Give your reasoning for the fraction you chose to divert. How risky do you think this experiment would be for Udacity?</span>

<span class="c13 c2"></span>

<span class="c1">Here I chosed 50% traffic for this experiment . Already registered students won’t be affected by this experiment . Only the new users will be affected so it won’t be High Risk for Udacity .</span>

<span class="c1"></span>

<span class="c1"></span>

# <span class="c22 c2">Experiment Analysis</span>

## <span class="c8"></span>

## <span class="c8">Sanity Checks</span>

<span class="c13 c2">For each of your invariant metrics, give the 95% confidence interval for the value you expect to observe, the actual observed value, and whether the metric passes your sanity check. (These should be the answers from the "Sanity Checks" quiz.)</span>

<span class="c13 c2"></span>

<span class="c0">Number of Cookies:</span>

<span class="c0"></span>

<a id="t.0fff211cfb9263fc24351d9ac079819b9a24beed"></a><a id="t.3"></a>

<table class="c32">

<tbody>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c0">Pageviews in Control Group</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c1">345543</span>

</td>

</tr>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c0">Pageviews in Experiment Group</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c1">344660</span>

</td>

</tr>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c0">Total Pageviews(N)</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c1">690203</span>

</td>

</tr>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c0">Probability of Pageview to be in Control Group or Experiment Group</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c1">.5</span>

</td>

</tr>

<tr class="c21">

<td class="c7" colspan="1" rowspan="1">

<span class="c0">Standard Error(SE)</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c1">sqrt(.5*(1-.5)/N) = 0.0006018</span>

</td>

</tr>

<tr class="c21">

<td class="c7" colspan="1" rowspan="1">

<span class="c0">Margin of Error(m)</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c1">SE*Z = SE*1.96 = 0.0011796</span>

</td>

</tr>

<tr class="c21">

<td class="c7" colspan="1" rowspan="1">

<span class="c0">Confidence Interval(CI)</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c1">0.5 (+-) m = [0.4988,0.5012]</span>

</td>

</tr>

<tr class="c21">

<td class="c7" colspan="1" rowspan="1">

<span class="c0">Observed Value</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c1">345543/690203 = 0.5006</span>

</td>

</tr>

</tbody>

</table>

<span class="c0"></span>

<span class="c0"></span>

<span class="c0">Observed Value 0.5006 in CI [0.4988,0.5012]</span>

<span class="c1">Hence Number of Cookies PASS Sanity Check</span>

<span class="c0"></span>

<span class="c0">Number of Clicks:</span>

<a id="t.103c2194b2ea394a1a07e1ed363cdd5d6b8fbba6"></a><a id="t.4"></a>

<table class="c32">

<tbody>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c0">Clicks in Control Group</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c1">28378</span>

</td>

</tr>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c0">Clicks in Experiment Group</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c1">28325</span>

</td>

</tr>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c0">Total Pageviews(N)</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c1">56703</span>

</td>

</tr>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c0">Probability of Pageview to be in Control Group or Experiment Group</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c1">.5</span>

</td>

</tr>

<tr class="c21">

<td class="c7" colspan="1" rowspan="1">

<span class="c0">Standard Error(SE)</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c1">sqrt(.5*(1-.5)/N) = 0.0021</span>

</td>

</tr>

<tr class="c21">

<td class="c7" colspan="1" rowspan="1">

<span class="c0">Margin of Error(m)</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c1">SE*Z = SE*1.96 = 0.0041</span>

</td>

</tr>

<tr class="c21">

<td class="c7" colspan="1" rowspan="1">

<span class="c0">Confidence Interval(CI)</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c1">0.5 (+-) m = [0.4959,0.5041]</span>

</td>

</tr>

<tr class="c21">

<td class="c7" colspan="1" rowspan="1">

<span class="c0">Observed Value</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c1">28378/56703=0.50046</span>

</td>

</tr>

</tbody>

</table>

<span class="c0"></span>

<span class="c0">Observed Value 0.50046 in CI [0.4959,0.5041]</span>

<span class="c1">Hence Number of Clicks PASS Sanity Check</span>

<span class="c0"></span>

<span class="c0"></span>

## <span class="c8">Result Analysis</span>

### <span class="c23 c9">Effect Size Tests</span>

<span class="c13 c2">For each of your evaluation metrics, give a 95% confidence interval around the difference between the experiment and control groups. Indicate whether each metric is statistically and practically significant. (These should be the answers from the "Effect Size Tests" quiz.)</span>

<span class="c13 c2"></span>

<span class="c0">GROSS CONVERSION:</span>

<span class="c1"></span>

<a id="t.c30bbe3b15ac2e3e6ca2fce04e71e1b937bd1b4f"></a><a id="t.5"></a>

<table class="c32">

<tbody>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c9">Clicks Control Group (N</span><span class="c16 c9">cont</span><span class="c0">)</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0">17293</span>

</td>

</tr>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c9">Enrollment Control Group (X</span><span class="c16 c9">cont</span><span class="c9">)</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0">3785</span>

</td>

</tr>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c9">Clicks Experiment Group(N</span><span class="c16 c9">exp</span><span class="c0">)</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0">17260</span>

</td>

</tr>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c9">Enrollment Experiment Group(X</span><span class="c16 c9">exp</span><span class="c0">)</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0">3423</span>

</td>

</tr>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c9">Gross Conversion Control Group(P</span><span class="c16 c9">cont</span><span class="c0">)</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0">0.218875</span>

</td>

</tr>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c9">Gross Conversion Experiment Group(P</span><span class="c16 c9">exp</span><span class="c0">)</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0">0.19832</span>

</td>

</tr>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c0">D-Hat</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0">-0.02055</span>

</td>

</tr>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c9">Pooled Probability (P</span><span class="c16 c9">pool</span> <span class="c9">)</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0">0.2086</span>

</td>

</tr>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c0">Standard Error (SE)</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0">0.00437</span>

</td>

</tr>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c0">Margin of Error (m)</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0">0.00857</span>

</td>

</tr>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c0">Confidence Interval</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0">[-0.02912,-0.01199]</span>

</td>

</tr>

</tbody>

</table>

<span class="c1"></span>

<span class="c2">Confidence Interval</span> <span class="c0">[-0.02912,-0.01199]</span>

<span class="c0">Statistically Significant - Dont Have 0 in CI</span>

<span class="c9">Practically Significant - CI does not contain d</span><span class="c15 c9">min</span>

<span class="c1"></span>

<span class="c1"></span>

<span class="c0">NET CONVERSION:</span>

<span class="c1"></span>

<a id="t.d285888383fb202b7717da33a0463427255d011b"></a><a id="t.6"></a>

<table class="c32">

<tbody>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c9">Clicks Control Group (N</span><span class="c16 c9">cont</span><span class="c0">)</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0">17293</span>

</td>

</tr>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c9">Payment Control Group (X</span><span class="c16 c9">cont</span><span class="c9">)</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0">2033</span>

</td>

</tr>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c9">Clicks Experiment Group(N</span><span class="c9 c16">exp</span><span class="c0">)</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0">17260</span>

</td>

</tr>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c9">Payment Experiment Group(X</span><span class="c16 c9">exp</span><span class="c0">)</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0">1945</span>

</td>

</tr>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c9">Net Conversion Control Group(P</span><span class="c16 c9">cont</span><span class="c0">)</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c9 c17">0.11756</span>

</td>

</tr>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c9">Net Conversion Experiment Group(P</span><span class="c16 c9">exp</span><span class="c0">)</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c9 c17">0.11268</span>

</td>

</tr>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c0">D-Hat</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0">-0.0049</span>

</td>

</tr>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c9">Pooled Probability (P</span><span class="c16 c9">pool</span> <span class="c9">)</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0">0.1151</span>

</td>

</tr>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c0">Standard Error (SE)</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0">0.00343</span>

</td>

</tr>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c0">Margin of Error (m)</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0">0.0067</span>

</td>

</tr>

<tr class="c14">

<td class="c7" colspan="1" rowspan="1">

<span class="c0">Confidence Interval</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c0">[-0.0116 , 0.0018]</span>

</td>

</tr>

</tbody>

</table>

<span class="c1"></span>

<span class="c0">Confidence Interval [-0.0116 , 0.0018]</span>

<span class="c0">Not Statistically Significant - CI contains 0</span>

<span class="c9">Not Practically Significant - CI contains d</span><span class="c15 c9">min</span>

<span class="c1"></span>

### <span class="c23 c9">Sign Tests</span>

<span class="c13 c2">For each of your evaluation metrics, do a sign test using the day-by-day data, and report the p-value of the sign test and whether the result is statistically significant. (These should be the answers from the "Sign Tests" quiz.)</span>

<span class="c13 c2"></span>

<span class="c0">GROSS CONVERSION</span>

<span class="c1"></span>

<a id="t.8ffe1533f67199c62f1f8b4369e27eff693e3233"></a><a id="t.7"></a>

<table class="c37">

<tbody>

<tr class="c14">

<td class="c10" colspan="1" rowspan="1">

<span class="c0">Number of Success</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c1">19</span>

</td>

</tr>

<tr class="c14">

<td class="c10" colspan="1" rowspan="1">

<span class="c0">Number of Experiments</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c1">23</span>

</td>

</tr>

<tr class="c14">

<td class="c10" colspan="1" rowspan="1">

<span class="c0">Probability</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c1">0.5</span>

</td>

</tr>

<tr class="c14">

<td class="c10" colspan="1" rowspan="1">

<span class="c0">Two Tailed P-value</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c1">0.0026</span>

</td>

</tr>

</tbody>

</table>

<span class="c1">As P-value (0.0026) < Alpha Level (0.025)</span>

<span class="c9 c17">S</span><span class="c0 c17">tatistically and practically significant.</span>

<span class="c0 c17"></span>

<span class="c0">NET CONVERSION</span>

<span class="c1"></span>

<a id="t.1f459765a37dad0e53dc60ab3bb0087838e4f204"></a><a id="t.8"></a>

<table class="c37">

<tbody>

<tr class="c14">

<td class="c10" colspan="1" rowspan="1">

<span class="c0">Number of Success</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c1">13</span>

</td>

</tr>

<tr class="c14">

<td class="c10" colspan="1" rowspan="1">

<span class="c0">Number of Experiments</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c1">23</span>

</td>

</tr>

<tr class="c14">

<td class="c10" colspan="1" rowspan="1">

<span class="c0">Probability</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c1">0.5</span>

</td>

</tr>

<tr class="c14">

<td class="c10" colspan="1" rowspan="1">

<span class="c0">Two Tailed P-value</span>

</td>

<td class="c7" colspan="1" rowspan="1">

<span class="c1">0.6776</span>

</td>

</tr>

</tbody>

</table>

<span class="c0 c17"></span>

<span class="c1">As P-value (0.6776) > Alpha Level (0.025)</span>

<span class="c0 c17">Statistically and practically Insignificant.</span>

<span class="c0 c17"></span>

<span class="c0 c17"></span>

<span class="c2 c24"></span>

### <span class="c2">Summary</span>

<span class="c29 c2">State whether you used the Bonferroni correction, and explain why or why not.</span> <span class="c13 c2">If there are any discrepancies between the effect size hypothesis tests and the sign tests, describe the discrepancy and why you think it arose.</span>

<span class="c13 c2"></span>

<span class="c2">No I will not use the Bonferroni correction because</span> <span class="c18 c17 c2">the metrics in the experiment has high correlation .We will only launch if we get a significant amount of change over all metrics . In this case there is no need of Bonferroni Correction.</span>

<span class="c13 c2"></span>

<span class="c1"></span>

## <span class="c8">Recommendation</span>

<span class="c13 c2">Make a recommendation and briefly describe your reasoning.</span>

<span class="c13 c2"></span>

<span class="c2">As we can see that Gross Conversion change is both statistically and practically significant and there is a high chance that the Gross Conversion will go down . By launching this feature we will discourage those students who cannot commit a certain amount of time every week to this course so our overall enrollment will go down which include the revenue too , though there is no significant change of Net Conversion both statistically and practically . YES Udacity should launch this feature , which will decrease the number of enrollments who don’t have enough time for this course , so more resource could be allocated for the students who can . Adding this feature won’t be a high risk in revenue because we don’t see any significant change in Net Conversion both Statistically and Practically .</span>

# <span class="c22 c2">Follow-Up Experiment</span>

<span class="c2 c29">Give a high-level description of the follow up experiment you would run, what your hypothesis would be, what metrics you would want to measure, what your unit of diversion would be, and your reasoning for these choices.</span>

<span class="c1"></span>

<span class="c1"></span>

<span class="c1">In the follow up experiment I would like that to have a quiz for the students for the First Free trail week that checks the knowledge a student should have before starting the Data Analyst Nanodegree which includes basic python knowledge , working in the Ipython notebook etc.</span>

<span class="c1"></span>

<span class="c1">I will evenly distribute the quiz between the control and the experiment groups , the students in the control group will not have the quiz on the other hand the experiment group students will have this quiz .</span>

<span class="c1"></span>

<span class="c9">Null Hypothesis (H</span><span class="c16 c9">0</span><span class="c0">) :</span>

<span class="c1">Adding the quiz don’t increase Retention .</span>

<span class="c1"></span>

<span class="c0">Metrics:</span>

<span class="c0">INVARIANT</span>

<span class="c1">Number of Unique users enrolled in the Course as Free Trial</span>

<span class="c1">As the number of unique users enrolled in the course is not dependent on the experiment as the experiment is staged after the user Starts the free Trial.</span>

<span class="c1"></span>

<span class="c0">EVALUATION</span>

<span class="c1">Number of unique users that actually makes the first payment .</span>

<span class="c1">As the number of unique users who make the first payment which will be done after the Trial Period where the experiment is staged . So these are chosen as Evaluation Metrics .</span>

<span class="c1"></span>

<span class="c0">Unit of Diversion:</span>

<span class="c1">User IDs will be the unit of diversion because here we will only experiment on the users who actually enrolled for the course as a Free Trial .</span>

<span class="c1"></span>

<span class="c1"></span>
