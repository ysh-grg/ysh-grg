"""
Module responsible to define all SQL queries to
generate the data sets for optimizer refresh.

It is separated from python code so we can
keep the code as clean as possible.
"""

class Queries(Base):
    """
    Class to initialize all SQL queries used across the optimizer service.
    """

    def __init__(self):

        super().__init__()

    # Query to get baseline sales for total beer
    baseline_sls = \
        "SELECT DATENAME(WEEK, inv_date) as week_num, " \
        "store_id, " \
        "UEN, " \
        "DRV, " \
        "poc_segmentation, " \
        "sub_test_id, " \
        "test_group, " \
        "sum(HLS) as volume, " \
        "sum(ING_2) as net_revenue, " \
        "sum(maco) as maco, " \
        "avg(days) as n_days " \
        "FROM abi_lh_az_testops.performance_indicators " \
        "INNER JOIN (" \
            "select u.sub_test_id, " \
            "test_details, " \
            "baseline_start_period, " \
            "baseline_end_period, " \
            "store_id, " \
            "test_group, " \
            "DATEDIFF(d, baseline_start_period, baseline_end_period) + 1 as days " \
            "from abi_lh_az_testops.experiment_universe u " \
            "inner join abi_lh_az_testops.experiment_geo_details g " \
                "on g.sub_test_id = u.sub_test_id " \
                "where u.pillar = '{PILLAR}' and u.month = '{MONTH}') p " \
                "on cliente = p.store_id " \
                "where " \
                    "(inv_date >= baseline_start_period AND inv_date <= baseline_end_period ) " \
                    "group by DATENAME(WEEK, inv_date), " \
                    "store_id, " \
                    "UEN, " \
                    "DRV, " \
                    "poc_segmentation, " \
                    "sub_test_id, " \
                    "test_group "
                    

    # Query to get treatment sales for total beer
    treatment_sls = \
        "SELECT DATENAME(WEEK, inv_date) as week_num, " \
        "store_id, " \
        "UEN, " \
        "DRV, " \
        "poc_segmentation, " \
        "sub_test_id, " \
        "test_group, " \
        "sum(HLS) as volume, " \
        "sum(ING_2) as net_revenue, " \
        "sum(maco) as maco, " \
        "avg(days) as n_days " \
        "FROM abi_lh_az_testops.performance_indicators " \
        "INNER JOIN (" \
            "select u.sub_test_id, " \
            "test_details, " \
            "analysis_start_period, " \
            "analysis_end_period, " \
            "store_id, " \
            "test_group, " \
            "DATEDIFF(d, analysis_start_period, analysis_end_period) + 1 as days " \
            "from abi_lh_az_testops.experiment_universe u " \
            "inner join abi_lh_az_testops.experiment_geo_details g " \
                "on g.sub_test_id = u.sub_test_id " \
                "where u.pillar = '{PILLAR}' and u.month = '{MONTH}') p " \
                "on cliente = p.store_id " \
                "where " \
                    "(inv_date >= analysis_start_period AND inv_date <= analysis_end_period ) " \
                    "group by DATENAME(WEEK, inv_date), " \
                    "store_id, " \
                    "UEN, " \
                    "DRV, " \
                    "poc_segmentation, " \
                    "sub_test_id, " \
                    "test_group "            
                    

    # Query to get baseline sales as per SKU details
    baseline_sku_sls = \
        "SELECT DATENAME(WEEK, inv_date) as week_num, " \
        "store_id, " \
        "UEN, " \
        "DRV, " \
        "poc_segmentation, " \
        "sub_test_id, " \
        "test_group, " \
        "sum(HLS) as volume, " \
        "sum(ING_2) as net_revenue, " \
        "sum(maco) as maco, " \
        "avg(days) as n_days " \
        "FROM abi_lh_az_testops.performance_indicators " \
        "INNER JOIN (" \
            "select u.sub_test_id, " \
            "test_details, " \
            "sku, " \
            "baseline_start_period, " \
            "baseline_end_period, " \
            "store_id, " \
            "test_group, " \
            "DATEDIFF(d, baseline_start_period, baseline_end_period) + 1 as days " \
            "from abi_lh_az_testops.experiment_universe u " \
            "inner join abi_lh_az_testops.experiment_geo_details g " \
            "inner join abi_lh_az_testops.b2b2c_audience_brands br " \
                "on br.audience_key = u.sub_test_id " \
                "on g.sub_test_id = u.sub_test_id " \
                "where u.pillar = '{PILLAR}' and u.month = '{MONTH}') p " \
                "on cliente = p.store_id " \
                "and material = p.sku " \
                "where " \
                    "(inv_date >= baseline_start_period AND inv_date <= baseline_end_period ) " \
                    "group by DATENAME(WEEK, inv_date), " \
                    "store_id, " \
                    "UEN, " \
                    "DRV, " \
                    "poc_segmentation, " \
                    "sub_test_id, " \
                    "test_group "
                    

    # Query to get treatment sales as per SKU details
    treatment_sku_sls = \
        "SELECT DATENAME(WEEK, inv_date) as week_num, " \
        "store_id, " \
        "UEN, " \
        "DRV, " \
        "poc_segmentation, " \
        "sub_test_id, " \
        "test_group, " \
        "sum(HLS) as volume, " \
        "sum(ING_2) as net_revenue, " \
        "sum(maco) as maco, " \
        "avg(days) as n_days " \
        "FROM abi_lh_az_testops.performance_indicators " \
        "INNER JOIN (" \
            "select u.sub_test_id, " \
            "test_details, " \
            "sku, " \
            "treatment_start_period, " \
            "treatment_end_period, " \
            "store_id, " \
            "test_group, " \
            "DATEDIFF(d, treatment_start_period, treatment_end_period) + 1 as days " \
            "from abi_lh_az_testops.experiment_universe u " \
            "inner join abi_lh_az_testops.experiment_geo_details g " \
            "inner join abi_lh_az_testops.b2b2c_audience_brands br " \
                "on br.audience_key = u.sub_test_id " \
                "on g.sub_test_id = u.sub_test_id " \
                "where u.pillar = '{PILLAR}' and u.month = '{MONTH}') p " \
                "on cliente = p.store_id " \
                "and material = p.sku " \
                "where " \
                    "(inv_date >= treatment_start_period AND inv_date <= treatment_end_period ) " \
                    "group by DATENAME(WEEK, inv_date), " \
                    "store_id, " \
                    "UEN, " \
                    "DRV, " \
                    "poc_segmentation, " \
                    "sub_test_id, " \
                    "test_group "
                    
    # Query to get treatment sales for total beer (temporary table)
    treatment_sls2 = \
        "SELECT DATENAME(WEEK, inv_date) as week_num, " \
        "store_id, " \
        "UEN, " \
        "DRV, " \
        "poc_segmentation, " \
        "sub_test_id, " \
        "test_group, " \
        "sum(HLS) as volume, " \
        "sum(ING_2) as net_revenue, " \
        "sum(maco) as maco, " \
        "avg(days) as n_days " \
        "FROM abi_lh_az_testops.revenue_nov " \
        "INNER JOIN (" \
            "select u.sub_test_id, " \
            "test_details, " \
            "analysis_start_period, " \
            "analysis_end_period, " \
            "store_id, " \
            "test_group, " \
            "DATEDIFF(d, analysis_start_period, analysis_end_period) + 1 as days " \
            "from abi_lh_az_testops.experiment_universe u " \
            "inner join abi_lh_az_testops.experiment_geo_details g " \
                "on g.sub_test_id = u.sub_test_id " \
                "where u.pillar = '{PILLAR}' and u.month = '{MONTH}') p " \
                "on cliente = p.store_id " \
                "where " \
                    "(Fecha_Pedido >= analysis_start_period AND Fecha_Pedido <= analysis_end_period ) " \
                    "group by DATENAME(WEEK, inv_date), " \
                    "store_id, " \
                    "UEN, " \
                    "DRV, " \
                    "poc_segmentation, " \
                    "sub_test_id, " \
                    "test_group "  