-- Write your query below
-- distinct students highest score with the other columbn as well
--smallest exam id tie breaker
--ordered by sid then descinding score then exam id

SELECT DISTINCT ON (student_id)
student_id, exam_id, score
FROM exam_results
ORDER BY student_id, score DESC, exam_id
;