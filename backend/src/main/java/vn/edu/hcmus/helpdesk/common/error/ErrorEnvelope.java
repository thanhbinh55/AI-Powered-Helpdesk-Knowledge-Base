package vn.edu.hcmus.helpdesk.common.error;

import com.fasterxml.jackson.annotation.JsonInclude;

import java.time.Instant;
import java.util.Map;

public record ErrorEnvelope(ErrorBody error) {

    @JsonInclude(JsonInclude.Include.NON_NULL)
    public record ErrorBody(
            ErrorCode code,
            String message,
            String requestId,
            Instant timestamp,
            Map<String, Object> details
    ) {}

    public static ErrorEnvelope of(ErrorCode code, String message, String requestId) {
        return new ErrorEnvelope(new ErrorBody(code, message, requestId, Instant.now(), null));
    }

    public static ErrorEnvelope of(ErrorCode code, String message, String requestId, Map<String, Object> details) {
        return new ErrorEnvelope(new ErrorBody(code, message, requestId, Instant.now(), details));
    }
}

