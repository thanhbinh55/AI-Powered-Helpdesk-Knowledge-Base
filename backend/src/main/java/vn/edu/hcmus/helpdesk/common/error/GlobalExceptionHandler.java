package vn.edu.hcmus.helpdesk.common.error;

import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.HttpStatusCode;
import org.springframework.http.ResponseEntity;
import org.springframework.http.converter.HttpMessageNotReadableException;
import org.springframework.lang.Nullable;
import org.springframework.validation.FieldError;
import org.springframework.web.HttpRequestMethodNotSupportedException;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.context.request.WebRequest;
import org.springframework.web.servlet.mvc.method.annotation.ResponseEntityExceptionHandler;

import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

@RestControllerAdvice
public class GlobalExceptionHandler extends ResponseEntityExceptionHandler {

    @ExceptionHandler(AppException.class)
    public ResponseEntity<ErrorEnvelope> handleAppException(AppException ex, WebRequest request) {
        String requestId = getOrCreateRequestId(request);
        ErrorEnvelope envelope = ErrorEnvelope.of(ex.getErrorCode(), ex.getMessage(), requestId);
        return ResponseEntity.status(ex.getHttpStatus()).body(envelope);
    }

    @Override
    @Nullable
    protected ResponseEntity<Object> handleExceptionInternal(
            Exception ex, @Nullable Object body, HttpHeaders headers, HttpStatusCode status, WebRequest request) {
        String requestId = getOrCreateRequestId(request);
        ErrorEnvelope envelope = switch (ex) {
            case MethodArgumentNotValidException validation -> validationError(validation, requestId);
            case HttpMessageNotReadableException ignored -> ErrorEnvelope.of(
                    ErrorCode.MALFORMED_JSON, "Định dạng JSON yêu cầu không hợp lệ hoặc thiếu body", requestId);
            case HttpRequestMethodNotSupportedException method -> ErrorEnvelope.of(
                    ErrorCode.METHOD_NOT_ALLOWED,
                    "Phương thức HTTP " + method.getMethod() + " không được hỗ trợ cho endpoint này", requestId);
            default -> switch (status.value()) {
                case 400 -> ErrorEnvelope.of(
                        ErrorCode.VALIDATION_FAILED, "Dữ liệu yêu cầu không hợp lệ", requestId);
                case 404 -> ErrorEnvelope.of(
                        ErrorCode.RESOURCE_NOT_FOUND, "Không tìm thấy tài nguyên", requestId);
                case 415 -> ErrorEnvelope.of(
                        ErrorCode.UNSUPPORTED_MEDIA_TYPE, "Định dạng nội dung không được hỗ trợ", requestId);
                default -> status.is4xxClientError()
                        ? ErrorEnvelope.of(ErrorCode.INVALID_REQUEST, "Yêu cầu không hợp lệ", requestId)
                        : internalError(requestId);
            };
        };
        return super.handleExceptionInternal(ex, envelope, headers, status, request);
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorEnvelope> handleGeneral(Exception ex, WebRequest request) {
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
                .body(internalError(getOrCreateRequestId(request)));
    }

    private ErrorEnvelope validationError(MethodArgumentNotValidException ex, String requestId) {
        Map<String, Object> details = new HashMap<>();
        for (FieldError fieldError : ex.getBindingResult().getFieldErrors()) {
            details.put(fieldError.getField(), fieldError.getDefaultMessage());
        }
        return ErrorEnvelope.of(
                ErrorCode.VALIDATION_FAILED, "Dữ liệu yêu cầu không hợp lệ", requestId, details);
    }

    private ErrorEnvelope internalError(String requestId) {
        return ErrorEnvelope.of(ErrorCode.INTERNAL_SERVER_ERROR, "Đã xảy ra lỗi máy chủ nội bộ", requestId);
    }

    private String getOrCreateRequestId(WebRequest request) {
        String reqId = request.getHeader("X-Request-Id");
        return (reqId != null && !reqId.isBlank()) ? reqId : UUID.randomUUID().toString();
    }
}
