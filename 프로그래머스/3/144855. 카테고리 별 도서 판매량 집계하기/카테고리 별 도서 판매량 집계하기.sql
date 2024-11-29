SELECT CATEGORY, SUM(BOOK_SALES.SALES) AS TOTAL_SALES
FROM BOOK
LEFT JOIN BOOK_SALES
ON BOOK.BOOK_ID = BOOK_SALES.BOOK_ID
WHERE BOOK_SALES.SALES_DATE LIKE '2022-01%'
GROUP BY BOOK.CATEGORY
ORDER BY BOOK.CATEGORY ASC;