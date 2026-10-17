// Digitized River for ANSYS DesignModeler

var XYPlane = agb.GetXYPlane();
agb.SetActivePlane(XYPlane);

var RiverSketch = XYPlane.newSketch();
RiverSketch.Name = "Digitized_River_3_Splines_Fixed";

// Riverbank 1: one spline through 40 fit points
var S1 = RiverSketch.SplineBegin();
with (S1)
{
    SplineFlexibility = agc.No;
    SplineXY(4712.5, 1739.37);
    SplineXY(4600.8, 1819.16);
    SplineXY(4473.15, 1909.58);
    SplineXY(4350.82, 2015.95);
    SplineXY(4233.8, 2117.01);
    SplineXY(4122.11, 2212.75);
    SplineXY(4026.37, 2297.85);
    SplineXY(3957.22, 2372.32);
    SplineXY(3877.44, 2446.78);
    SplineXY(3787.02, 2542.52);
    SplineXY(3701.92, 2632.94);
    SplineXY(3616.82, 2734);
    SplineXY(3552.99, 2813.78);
    SplineXY(3478.53, 2914.84);
    SplineXY(3398.74, 3021.22);
    SplineXY(3334.92, 3132.91);
    SplineXY(3292.37, 3271.2);
    SplineXY(3260.45, 3372.26);
    SplineXY(3233.86, 3478.64);
    SplineXY(3191.31, 3616.93);
    SplineXY(3159.4, 3728.62);
    SplineXY(3127.48, 3850.96);
    SplineXY(3090.25, 3967.97);
    SplineXY(3053.02, 4106.26);
    SplineXY(3015.79, 4233.91);
    SplineXY(2989.19, 4345.61);
    SplineXY(2957.28, 4457.3);
    SplineXY(2930.69, 4558.36);
    SplineXY(2898.77, 4659.42);
    SplineXY(2872.18, 4760.48);
    SplineXY(2840.26, 4866.86);
    SplineXY(2803.03, 5010.46);
    SplineXY(2771.12, 5111.52);
    SplineXY(2733.89, 5239.17);
    SplineXY(2701.97, 5356.19);
    SplineXY(2670.06, 5473.2);
    SplineXY(2627.51, 5622.13);
    SplineXY(2584.96, 5760.42);
    SplineXY(2553.05, 5877.44);
    SplineXY(2515.82, 6031.68);
    SplineFitPtEnd();
}

// Riverbank 2: one spline through 47 fit points
var S2 = RiverSketch.SplineBegin();
with (S2)
{
    SplineFlexibility = agc.No;
    SplineXY(3765.74, 510.72);
    SplineXY(3723.19, 590.5);
    SplineXY(3670.01, 691.56);
    SplineXY(3627.45, 781.98);
    SplineXY(3574.27, 909.63);
    SplineXY(3542.35, 1016.01);
    SplineXY(3521.08, 1143.66);
    SplineXY(3505.12, 1271.31);
    SplineXY(3489.16, 1393.65);
    SplineXY(3478.53, 1500.02);
    SplineXY(3457.25, 1606.4);
    SplineXY(3441.29, 1718.1);
    SplineXY(3398.74, 1851.07);
    SplineXY(3366.83, 1968.08);
    SplineXY(3340.24, 2085.1);
    SplineXY(3303, 2212.75);
    SplineXY(3271.09, 2324.45);
    SplineXY(3244.5, 2436.14);
    SplineXY(3207.27, 2563.79);
    SplineXY(3170.03, 2696.77);
    SplineXY(3132.8, 2813.78);
    SplineXY(3100.89, 2936.11);
    SplineXY(3074.29, 3063.77);
    SplineXY(3037.06, 3186.1);
    SplineXY(3005.15, 3297.8);
    SplineXY(2978.55, 3414.81);
    SplineXY(2941.32, 3526.51);
    SplineXY(2904.09, 3654.16);
    SplineXY(2866.86, 3776.49);
    SplineXY(2829.63, 3914.78);
    SplineXY(2797.71, 4031.8);
    SplineXY(2755.16, 4186.04);
    SplineXY(2712.61, 4319.01);
    SplineXY(2680.7, 4451.99);
    SplineXY(2643.47, 4579.64);
    SplineXY(2616.87, 4701.97);
    SplineXY(2574.32, 4834.94);
    SplineXY(2542.41, 4957.28);
    SplineXY(2505.18, 5079.61);
    SplineXY(2478.58, 5191.31);
    SplineXY(2446.67, 5318.96);
    SplineXY(2414.76, 5441.29);
    SplineXY(2382.84, 5547.67);
    SplineXY(2340.29, 5696.6);
    SplineXY(2308.38, 5797.65);
    SplineXY(2276.47, 5898.71);
    SplineXY(2260.51, 5967.86);
    SplineFitPtEnd();
}

// Riverbank 3: one spline through 42 fit points
var S3 = RiverSketch.SplineBegin();
with (S3)
{
    SplineFlexibility = agc.No;
    SplineXY(4648.67, 1659.59);
    SplineXY(4574.21, 1718.1);
    SplineXY(4483.79, 1781.92);
    SplineXY(4388.05, 1861.71);
    SplineXY(4302.95, 1936.17);
    SplineXY(4191.25, 2026.59);
    SplineXY(4095.51, 2106.37);
    SplineXY(3994.45, 2202.11);
    SplineXY(3893.4, 2297.85);
    SplineXY(3797.66, 2398.91);
    SplineXY(3717.87, 2484.01);
    SplineXY(3627.45, 2579.75);
    SplineXY(3542.35, 2680.81);
    SplineXY(3499.8, 2739.32);
    SplineXY(3462.57, 2781.87);
    SplineXY(3430.66, 2819.1);
    SplineXY(3398.74, 2861.65);
    SplineXY(3377.47, 2893.56);
    SplineXY(3356.19, 2925.48);
    SplineXY(3324.28, 2946.75);
    SplineXY(3324.28, 2909.52);
    SplineXY(3334.92, 2872.29);
    SplineXY(3345.56, 2835.06);
    SplineXY(3356.19, 2797.82);
    SplineXY(3372.15, 2744.63);
    SplineXY(3398.74, 2659.53);
    SplineXY(3430.66, 2558.48);
    SplineXY(3457.25, 2462.74);
    SplineXY(3494.48, 2367);
    SplineXY(3515.76, 2239.34);
    SplineXY(3552.99, 2106.37);
    SplineXY(3595.54, 1957.45);
    SplineXY(3638.09, 1803.2);
    SplineXY(3685.96, 1648.95);
    SplineXY(3701.92, 1531.94);
    SplineXY(3728.51, 1393.65);
    SplineXY(3755.11, 1202.17);
    SplineXY(3781.7, 1069.2);
    SplineXY(3818.93, 952.18);
    SplineXY(3861.48, 840.49);
    SplineXY(3919.99, 723.47);
    SplineXY(3978.5, 627.73);
    SplineFitPtEnd();
}

// Fix each complete riverbank spline, including its endpoints.
XYPlane.FixedCon(S1, 1);
XYPlane.FixedCon(S2, 1);
XYPlane.FixedCon(S3, 1);

// Evaluate constraints and regenerate.
XYPlane.EvalDimCons();
agb.Regen();
