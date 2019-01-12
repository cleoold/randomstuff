#lang racket

;; as what the code expects!

(define (f-ai)
  (define my-text (read-line))
  (if
   (let ([last-word (last (string->list my-text))])
     (or (char=? last-word #\？) (char=? last-word #\?)))
   ((printf "~a！\n" (substring my-text 0 (- (string-length my-text) 2)))
    (f-ai))
   ((printf "~a！\n" (substring my-text 0 (string-length my-text)))
    (f-ai))))

(f-ai)

#| example
> 在吗？
在！
> 能听懂国语吗？
能听懂国语！
> 真的吗？
真的！
|#;

#|=========================================================================================
with some aids so it is shorter!

#lang racket

(require racket/string)

(define (f-ai)
  (define my-text (read-line))
  ((printf "~a\n"
           (string-replace
            (string-replace
             (string-replace my-text "吗" "") "？" "！") "?" "！"))
   (f-ai)))

(f-ai)
|#;
