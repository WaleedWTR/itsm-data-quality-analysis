-- Category mismatch count
SELECT
    original_category,
    COUNT(*) AS mismatch_count
FROM incidents
WHERE original_category <> validated_category
GROUP BY original_category
ORDER BY mismatch_count DESC;

-- Priority mismatch
SELECT
    incident_id,
    priority,
    expected_priority,
    short_description
FROM incidents
WHERE priority <> expected_priority;

-- Generic / low-value category usage
SELECT
    COUNT(*) AS other_category_count
FROM incidents
WHERE LOWER(original_category) = 'other';

-- Resolver distribution
SELECT
    resolver,
    COUNT(*) AS incident_count
FROM incidents
GROUP BY resolver
ORDER BY incident_count DESC;
