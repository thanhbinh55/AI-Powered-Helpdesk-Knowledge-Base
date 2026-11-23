package vn.edu.hcmus.helpdesk.common.error;

import jakarta.validation.Valid;
import jakarta.validation.constraints.NotBlank;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.context.annotation.Import;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.RequestBuilder;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.UUID;
import java.util.stream.Stream;

import static org.hamcrest.Matchers.containsString;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.header;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@WebMvcTest(GlobalExceptionHandlerTest.TestController.class)
@Import(GlobalExceptionHandlerTest.TestController.class)
class GlobalExceptionHandlerTest {
    @Autowired
    private MockMvc mvc;

    @ParameterizedTest
    @MethodSource("invalidRequests")
    void preservesClientErrorStatus(RequestBuilder request, int expectedStatus, String expectedCode) throws Exception {
        mvc.perform(request)
                .andExpect(status().is(expectedStatus))
                .andExpect(jsonPath("$.error.code").value(expectedCode));
    }

    static Stream<Arguments> invalidRequests() {
        return Stream.of(
                Arguments.of(get("/missing-route"), 404, "RESOURCE_NOT_FOUND"),
                Arguments.of(post("/probe").contentType(MediaType.TEXT_PLAIN).content("text"),
                        415, "UNSUPPORTED_MEDIA_TYPE"),
                Arguments.of(get("/probe/not-a-uuid"), 400, "VALIDATION_FAILED"),
                Arguments.of(post("/probe").contentType(MediaType.APPLICATION_JSON).content("{"),
                        400, "MALFORMED_JSON")
        );
    }

    @Test
    void preservesAllowHeaderForUnsupportedMethod() throws Exception {
        mvc.perform(get("/probe").header("X-Request-Id", "request-42"))
                .andExpect(status().isMethodNotAllowed())
                .andExpect(header().string(HttpHeaders.ALLOW, containsString("POST")))
                .andExpect(jsonPath("$.error.code").value("METHOD_NOT_ALLOWED"))
                .andExpect(jsonPath("$.error.requestId").value("request-42"));
    }

    @Test
    void preservesFieldValidationDetails() throws Exception {
        mvc.perform(post("/probe").contentType(MediaType.APPLICATION_JSON).content("{}"))
                .andExpect(status().isBadRequest())
                .andExpect(jsonPath("$.error.code").value("VALIDATION_FAILED"))
                .andExpect(jsonPath("$.error.details.name").isString());
    }

    @RestController
    static class TestController {
        @PostMapping(path = "/probe", consumes = MediaType.APPLICATION_JSON_VALUE)
        String submit(@Valid @RequestBody Payload payload) {
            return payload.name();
        }

        @GetMapping("/probe/{id}")
        String getById(@PathVariable UUID id) {
            return id.toString();
        }
    }

    record Payload(@NotBlank String name) {}
}
