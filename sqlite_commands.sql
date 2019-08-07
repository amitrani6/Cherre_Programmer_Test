INSERT INTO frequent_browsers (person_id, num_sites_visited)
           SELECT personId, SUM(unique_sites) AS unique_site_visits FROM(
               SELECT personId, COUNT(DISTINCT personId) AS unique_sites FROM visits
                   GROUP BY personId, siteId
                       )
             GROUP BY personId
             ORDER BY unique_site_visits DESC
             LIMIT 10;