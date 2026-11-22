package vn.edu.hcmus.helpdesk.common.error;

import jakarta.servlet.http.HttpServletRequest;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.http.converter.HttpMessageNotReadableException;
import org.springframework.validation.FieldError;
import org.springframework.web.HttpRequestMethodNotSupportedException;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(AppException.class)
    public ResponseEntity<ErrorEnvelope> handleAppException(AppException ex, HttpServletRequest request) {
        String requestId = getOrCreateRequestId(request);
        ErrorEnvelope envelope = ErrorEnvelope.of(ex.getErrorCode(), ex.getMessage(), requestId);
        return ResponseEntity.status(ex.getHttpStatus()).body(envelope);
    }

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ErrorEnvelope> handleValidation(MethodArgumentNotValidException ex, HttpServletRequest request) {
        String requestId = getOrCreateRequestId(request);
        Map<String, Object> details = new HashMap<>();
        for (FieldError fieldError : ex.getBindingResult().getFieldErrors()) {
            details.put(fieldError.getField(), fieldError.getDefaultMessage());
        }
        ErrorEnvelope envelope = ErrorEnvelope.of(
                ErrorCode.VALIDATION_FAILED,
                "Dữ liệu yêu cầu không hợp lệ",
                requestId,
                details
        );
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(envelope);
    }

    @ExceptionHandler(HttpMessageNotReadableException.class)
    public ResponseEntity<ErrorEnvelope> handleHttpMessageNotReadable(HttpMessageNotReadableException ex, HttpServletRequest request) {
        String requestId = getOrCreateRequestId(request);
        ErrorEnvelope envelope = ErrorEnvelope.of(
                ErrorCode.MALFORMED_JSON,
                "Định dạng JSON yêu cầu không hợp lệ hoặc thiếu body",
                requestId
        );
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(envelope);
    }

    @ExceptionHandler(HttpRequestMethodNotSupportedException.class)
    public ResponseEntity<ErrorEnvelope> handleMethodNotSupported(HttpRequestMethodNotSupportedException ex, HttpServletRequest request) {
        String requestId = getOrCreateRequestId(request);
        ErrorEnvelope envelope = ErrorEnvelope.of(
                ErrorCode.METHOD_NOT_ALLOWED,
                "Phương thức HTTP " + ex.getMethod() + " không được hỗ trợ cho endpoint này",
                requestId
        );
        return ResponseEntity.status(HttpStatus.METHOD_NOT_ALLOWED).body(envelope);
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorEnvelope> handleGeneral(Exception ex, HttpServletRequest request) {
        String requestId = getOrCreateRequestId(request);
        ErrorEnvelope envelope = ErrorEnvelope.of(
                ErrorCode.INTERNAL_SERVER_ERROR,
                "Đã xảy ra lỗi máy chủ nội bộ",
                requestId
        );
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(envelope);
    }

    private String getOrCreateRequestId(HttpServletRequest request) {
        String reqId = request.getHeader("X-Request-Id");
        return (reqId != null && !reqId.isBlank()) ? reqId : UUID.randomUUID().toString();
    }
}

